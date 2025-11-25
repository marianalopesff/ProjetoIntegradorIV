from transformers import AutoTokenizer, AutoModelForSequenceClassification
from deep_translator import GoogleTranslator
import torch
import re

# Carregar modelo treinado
tokenizer = AutoTokenizer.from_pretrained("backend/modelo_treinado")
model = AutoModelForSequenceClassification.from_pretrained("backend/modelo_treinado")

def limpar_texto(texto):
    texto = texto.lower()
    texto = re.sub(r'\s+', ' ', texto)
    texto = re.sub(r'[^a-zA-ZÀ-ÿ0-9.,;:!?() ]', '', texto)
    return texto.strip()

def traduzir_para_ingles(texto):
    try:
        return GoogleTranslator(source='auto', target='en').translate(texto)
    except Exception as e:
        print(f"⚠️ Erro ao traduzir: {e}")
        return texto  # caso falhe, usa o texto original

def analisar_texto(texto):
    texto = limpar_texto(texto)
    
    # Traduzir para inglês antes de analisar
    texto_en = traduzir_para_ingles(texto)
    print(f"🗣️ Texto traduzido: {texto_en}")  # apenas para debug
    
    inputs = tokenizer(texto_en, return_tensors="pt", truncation=True, padding=True, max_length=256)

    with torch.no_grad():
        outputs = model(**inputs)
        probs = torch.softmax(outputs.logits, dim=1)
        pred = torch.argmax(probs, dim=1).item()

    if pred == 0:
        return "✅ Bom: boas práticas e transparência."
    elif pred == 1:
        return "⚠️ Neutro: genérico, poderia melhorar."
    else:
        return "❌ Ruim: coleta de dados, cookies ou falta de privacidade."

def analisar_arquivo(caminho_txt):
    with open(caminho_txt, "r", encoding="utf-8", errors="ignore") as f:
        texto = f.read()
    resultado = analisar_texto(texto)
    print(f"Arquivo: {caminho_txt}\nResultado: {resultado}")
