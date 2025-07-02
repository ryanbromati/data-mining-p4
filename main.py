from pathlib import Path
from arima_sarima import analyze_dataset, run_arima_sarima
from text_mining import load_texts_from_csv, word_count, tfidf, lda
from web_scraping import scrape_news
import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    dataset = {
        'file': Path('./data/bcdata.sgs.22709_02.csv'),
        'name': 'Balança Comercial - Saldo Mensal',
        'unit': 'US$ milhões',
        'color': 'green'
    }

    clear_console()
    print("=== Análise de Séries Temporais ===")
    df = analyze_dataset(dataset['file'], dataset['name'], dataset['unit'], dataset['color'])
    run_arima_sarima(df, dataset['name'])

    input("\nPressione Enter para continuar...")

    clear_console()
    print("=== Web Scraping ===")
    scrape_news()  # Gera CSV em 'result-web-scraping/noticias_hackernews_rss.csv'

    input("\nPressione Enter para continuar...")

    clear_console()
    print("=== Mineração de Texto ===")
    texts = load_texts_from_csv('result-web-scraping/noticias_hackernews_rss.csv', column='Título')
    word_count(texts)
    tfidf(texts)
    lda(texts)
