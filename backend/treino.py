import os
import pandas as pd
import re
import torch
from sklearn.model_selection import train_test_split
from torch.utils.data import Dataset
from transformers import AutoTokenizer, AutoModelForSequenceClassification, Trainer, TrainingArguments

# Desativar W&B
os.environ["WANDB_DISABLED"] = "true"

# Caminho para os arquivos .txt do dataset
base_path = r"C:\Users\Asus\.cache\kagglehub\datasets\sonu1607\tosdr-terms-of-service-corpus\versions\1\text"
files = os.listdir(base_path)

# 1️⃣ Carregar dataset
data = []
for file in files:
    with open(os.path.join(base_path, file), "r", encoding="utf-8", errors="ignore") as f:
        texto = f.read()
        data.append({"arquivo": file, "texto": texto})

df = pd.DataFrame(data)

# 2️⃣ Limpar textos
def limpar_texto(texto):
    texto = texto.lower()
    texto = re.sub(r'\s+', ' ', texto)
    texto = re.sub(r'[^a-zA-ZÀ-ÿ0-9.,;:!?() ]', '', texto)
    return texto.strip()

df["texto_limpo"] = df["texto"].apply(limpar_texto)

# 3️⃣ Gerar labels automáticas
def gerar_label(texto):
    if any(p in texto for p in ["compartilhar dados", "publicidade", "terceiros", "cookies", "armazenar informações"]):
        return 2  # ruim
    elif any(p in texto for p in ["direito", "privacidade", "proteger dados", "excluir conta", "transparente"]):
        return 0  # bom
    else:
        return 1  # neutro

df["classe"] = df["texto_limpo"].apply(gerar_label)

# 4️⃣ Tokenização
model_name = "distilbert-base-uncased"
tokenizer = AutoTokenizer.from_pretrained(model_name)
tokens = tokenizer(df["texto_limpo"].tolist(), padding=True, truncation=True, max_length=256, return_tensors="pt")

# 5️⃣ Separar treino/teste
X_train, X_test, y_train, y_test = train_test_split(tokens["input_ids"], df["classe"].values, test_size=0.2, random_state=42)

# 6️⃣ Dataset PyTorch
class ContratoDataset(Dataset):
    def __init__(self, input_ids, labels):
        self.input_ids = input_ids
        self.labels = labels

    def __len__(self):
        return len(self.input_ids)

    def __getitem__(self, idx):
        return {"input_ids": self.input_ids[idx], "labels": torch.tensor(self.labels[idx])}

train_dataset = ContratoDataset(X_train, y_train)
test_dataset = ContratoDataset(X_test, y_test)

# 7️⃣ Modelo
model = AutoModelForSequenceClassification.from_pretrained(model_name, num_labels=3)

# 8️⃣ Treinamento
training_args = TrainingArguments(
    output_dir="./results",
    learning_rate=2e-5,
    per_device_train_batch_size=4,
    num_train_epochs=2,
    weight_decay=0.01,
    logging_dir="./logs"
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=test_dataset
)

trainer.train()

# 9️⃣ Salvar modelo e tokenizer
model.save_pretrained("./modelo_treinado")
tokenizer.save_pretrained("./modelo_treinado")
print("✅ Modelo treinado e salvo em ./modelo_treinado")