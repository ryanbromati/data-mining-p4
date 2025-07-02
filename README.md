# Avaliação N3 – Análise de Séries Temporais, Mineração de Texto e Web Scraping

## Objetivo

Verificar o entendimento sobre modelos ARIMA e SARIMA em séries temporais, técnicas de mineração de texto e aplicação de Web Scraping. A avaliação foi dividida em três partes:

---

## 1) ARIMA e SARIMA com Dados do Banco Central (3,0 pts)

**Dataset utilizado:**  
[Balança Comercial - Saldo Mensal](https://dadosabertos.bcb.gov.br)

**Ferramentas:**  
- Python  
- Bibliotecas: `pandas`, `matplotlib`, `statsmodels`, `scipy`

**Etapas realizadas:**
- Leitura e processamento da série temporal (`data`, `valor`)
- Cálculo da tendência por regressão linear (classificação: crescente/decrescente/estável)
- Aplicação dos modelos ARIMA(1,1,1) e SARIMA(1,1,1)x(1,1,1,12)
- Previsão dos próximos 12 meses
- Exibição dos gráficos e impressão dos resultados completos no terminal

**Resultados gerados:**
- Tendência geral: **Crescente**, inclinação: 56.7474, R²: 0.7676
- **Resumo ARIMA:** Log-Likelihood: -3161.857, AIC: 6329.714
- **Resumo SARIMA:** Log-Likelihood: -3037.424, AIC: 6084.848
- Gráficos:  
  1. Série temporal com linha de tendência  
  2. Previsão ARIMA vs SARIMA (12 meses)

---

## 2) Mineração de Texto com Três Técnicas (4,0 pts)

**Textos utilizados:**
```text
"O Brasil é o maior exportador de soja."
"A inflação no país tem subido nos últimos meses."
"O desemprego caiu, mas ainda preocupa."
```

**Técnicas aplicadas:**
- **Bag-of-Words (CountVectorizer)**  
- **TF-IDF (TfidfVectorizer)**  
- **LDA (Latent Dirichlet Allocation)**

**Ferramentas:**  
`sklearn`, `pandas`

**Resultados:**  
Os resultados de contagem de palavras, TF-IDF e tópicos LDA foram impressos no console. Cada técnica revelou diferentes insights sobre a relevância e estrutura semântica dos textos.

---

## 3) Web Scraping com RSS (3,0 pts)

**Fonte de dados:**  
[The Hacker News - RSS Feed](https://feeds.feedburner.com/TheHackersNews)

**Método:**  
- Leitura do feed RSS com `feedparser`
- Extração dos campos: **Título**, **Link**, **Resumo**
- Armazenamento dos dados no arquivo `result-web-scraping/noticias_hackernews_rss.csv`

**Exemplo de dados extraídos:**
```json
{
  "Título": "North Korean Hackers Target Web3 with Nim Malware and Use ClickFix in BabyShark Campaign",
  "Link": "https://thehackernews.com/2025/07/north-korean-hackers-target-web3-with.html",
  "Resumo": "Threat actors with ties to North Korea have been observed targeting Web3..."
}
```

```json
{
  "Título": "That Network Traffic Looks Legit, But it Could be Hiding a Serious Threat",
  "Link": "https://thehackernews.com/2025/07/that-network-traffic-looks-legit-but-it.html",
  "Resumo": "With nearly 80% of cyber threats now mimicking legitimate user behavior..."
}
```

**Resultado:**  
O CSV foi salvo com todas as notícias disponíveis, cada uma contendo os três campos descritos.

---

## Conclusão

Todos os itens da avaliação foram implementados conforme solicitado, com demonstração clara de aplicação dos modelos ARIMA/SARIMA, uso prático de técnicas de mineração de texto e Web Scraping com RSS. O projeto está estruturado para apresentação com saída visual (gráficos) e textual (console + CSV).