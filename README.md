# 📊 Análise de Séries Temporais, Mineração de Texto e Web Scraping

Trabalho prático integrando análise de séries temporais (ARIMA e SARIMA), mineração de texto (NLP) e web scraping de notícias.

---

## ✅ Questão 1 – ARIMA e SARIMA

### Objetivo
Analisar a tendência da série temporal da balança comercial (saldo mensal) e gerar previsões para os próximos 12 meses.

### Resultados principais

- Tendência: CRESCENTE  
- Inclinação: 56.7474  
- R²: 0.7676  

**Modelos e Previsões:**

| Modelo | AIC     | Descrição                  |
|--------|---------|----------------------------|
| ARIMA  | 6329.714| Modelo básico sem sazonalidade |
| SARIMA | 6084.848| Modelo com sazonalidade anual |

Previsões SARIMA para 12 meses: variam entre 22.900 e 25.000 (em US$ milhões).

---

## ✅ Questão 2 – Mineração de Texto

### Objetivo
Analisar textos reais extraídos do web scraping para identificar palavras frequentes, importância relativa e tópicos.

### Textos utilizados
Extraídos do arquivo CSV gerado pelo web scraping (títulos das notícias).

### Resultados

**Top 10 Palavras por Contagem:**

| Palavra   | Frequência |
|-----------|------------|
| to        | 18         |
| and       | 17         |
| in        | 15         |
| for       | 9          |
| attacks   | 6          |
| malware   | 6          |
| microsoft | 6          |
| new       | 6          |
| ai        | 5          |
| critical  | 5          |

**Top 10 Palavras por TF-IDF Médio:**

| Palavra   | TF-IDF Médio |
|-----------|--------------|
| to        | 0.0549       |
| and       | 0.0535       |
| in        | 0.0495       |
| for       | 0.0365       |
| malware   | 0.0284       |
| attacks   | 0.0274       |
| microsoft | 0.0269       |
| new       | 0.0260       |
| the       | 0.0250       |
| ai        | 0.0244       |

**Tópicos (LDA):**

- Tópico 1: to, and, in  
- Tópico 2: in, and, to  

---

## ✅ Questão 3 – Web Scraping

### Objetivo
Extrair notícias recentes para enriquecer a análise textual.

### Fonte utilizada
- [The Hacker News RSS](https://feeds.feedburner.com/TheHackersNews)

### Dados extraídos
Título, link e resumo das últimas notícias foram coletados e salvos em:

`result-web-scraping/noticias_hackernews_rss.csv`

---

## 🚀 Como executar o projeto

1. Instale as dependências usando o arquivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

2. Execute o programa principal:


```bash
python main.py
```