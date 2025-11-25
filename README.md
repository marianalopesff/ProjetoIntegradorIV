# Projeto Integrador IV

**EULA Simplificado – Analisador Automático de Termos de Uso e Políticas de Privacidade**

---

## Descrição do Projeto

O projeto consiste em desenvolver uma aplicação web capaz de receber contratos de software, aplicativos ou serviços online (EULAs, termos de uso, políticas de privacidade) e gerar automaticamente:

* **Resumo em linguagem simples**, facilitando a compreensão do usuário;
* **Destaque de riscos em categorias específicas**, como:

  * Coleta e compartilhamento de dados pessoais
  * Cobranças automáticas ou escondidas
  * Compartilhamento de informações com terceiros
  * Jurisdição ou obrigações legais

---

## Grupo

* **Rogelio Soares**
* **Mariana Lopes**
* **Jordhan Fernandes**
* **Murilo da Silva**
* **Lucas Xavier**

---

## Justificativa do Tema

A maioria dos usuários digitais aceita contratos e políticas de privacidade sem ler, devido à linguagem técnica e à extensão dos documentos. Isso os expõe a riscos como **coleta excessiva de dados**, **cobranças inesperadas** e **uso indevido de informações pessoais**.

Um sistema automatizado que simplifique os termos e destaque os principais riscos ajuda a:

* Aumentar a consciência digital dos usuários
* Reduzir incidentes de exposição de dados
* Proporcionar transparência em serviços digitais

---

## Métricas de Impacto

* Número de contratos analisados
* Quantidade de riscos detectados e destacados
* Feedback dos usuários sobre clareza e utilidade do resumo
* Medição do tempo economizado na leitura de contratos

---

## Sociedade Impactada

* **Usuários digitais**: alunos, profissionais e consumidores de apps e serviços online
* **Pequenos negócios e startups**: ao contratar serviços ou analisar EULAs de fornecedores
* **Instituições de ensino e serviços digitais**: que precisam avaliar termos de uso de plataformas utilizadas internamente

**Impacto:** maior compreensão e proteção legal/privacidade, reduzindo riscos de abuso e destacando informações importantes de forma acessível.

---

## Ferramentas e Tecnologias

* **Hugging Face Transformers** e **PyTorch** — utilizados para o treinamento e fine-tuning do modelo de IA (baseado no **DistilBERT**) para análise e classificação de textos contratuais.
* **Deep Translator** — responsável pela tradução automática dos textos para o inglês antes da análise, garantindo compatibilidade com o modelo.
* **Scikit-learn** — utilizado na divisão dos dados em conjuntos de treino e teste, além do suporte à validação.
* **Regex** e **Pandas** — empregados na limpeza, pré-processamento e organização dos textos de entrada.
* **Flask** — framework backend responsável por receber os textos e retornar os resultados da análise do modelo.
* **Vue.js** e **Tailwind CSS** — tecnologias aplicadas no desenvolvimento do frontend, garantindo uma interface moderna e responsiva. (EM DESENVOLVIMENTO...)
* **Dataset público (Kaggle – ToS;DR Corpus)** — base real de termos de serviço utilizada para o treinamento e testes do modelo.

---

## Resumo do Funcionamento do Sistema

O sistema funciona de maneira integrada entre **Inteligência Artificial**, **tradução automática** e **interface web**, permitindo que o usuário compreenda de forma simples os principais riscos e pontos de atenção em contratos e políticas de privacidade.

### Etapas do Processo

1. **Entrada do Texto**
   O usuário insere o conteúdo do contrato (ou termo de uso) diretamente na aplicação web.

2. **Pré-processamento**
   O texto é limpo e padronizado — removendo símbolos, espaçamentos e caracteres desnecessários — para facilitar a análise automática.

3. **Tradução Automática**
   O texto é traduzido para o inglês, garantindo compatibilidade com o modelo de linguagem utilizado na classificação.

4. **Análise com Inteligência Artificial**
   O modelo de IA, treinado com dados reais de termos de serviço, identifica o tom e o nível de risco do texto, classificando-o em três categorias:

   * **Bom:** boas práticas e transparência
   * **Neutro:** linguagem genérica, sem grandes riscos
   * **Ruim:** possíveis riscos à privacidade ou coleta indevida de dados

5. **Exibição dos Resultados**
   O sistema retorna a análise de forma clara e resumida na própria interface web, destacando os principais pontos identificados.

---

### Fluxo Simplificado do Sistema

```
Usuário 
   ↓
Interface Web (Flask) - Protótipo
   ↓
Pré-processamento e Tradução
   ↓
Modelo de IA (Transformers + PyTorch)
   ↓
Classificação do Texto
   ↓
Resultado e Resumo exibidos ao usuário
```

---


## Links

* **Dataset:** [ToSDR Terms of Service Corpus](https://www.kaggle.com/datasets/sonu1607/tosdr-terms-of-service-corpus)
* **Apresentação Protótipo:** [Vídeo do Protótipo](https://youtu.be/t9gtAb8C5UM)
* **Apresentação MVP:** [Vídeo do MVP](https://www.youtube.com/watch?v=cY1MJ5I93Uc)

