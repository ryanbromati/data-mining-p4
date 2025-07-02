import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.decomposition import LatentDirichletAllocation
from rich.console import Console
from rich.table import Table
from collections import Counter
import numpy as np

console = Console()

def load_texts_from_csv(filepath, column="Título"):
    df = pd.read_csv(filepath, encoding="utf-8")
    texts = df[column].dropna().astype(str).tolist()
    return texts

def word_count(texts, top_n=10):
    vectorizer = CountVectorizer()
    counts = vectorizer.fit_transform(texts)
    words = vectorizer.get_feature_names_out()
    sum_counts = np.array(counts.sum(axis=0)).flatten()
    freq = list(zip(words, sum_counts))
    freq.sort(key=lambda x: x[1], reverse=True)
    freq = freq[:top_n]

    table = Table(title=f"Top {top_n} Palavras - Contagem")
    table.add_column("Palavra", style="bold")
    table.add_column("Frequência", justify="right")

    for word, count in freq:
        table.add_row(word, str(count))
    console.print(table)

def tfidf(texts, top_n=10):
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(texts)
    words = vectorizer.get_feature_names_out()
    mean_tfidf = np.array(tfidf_matrix.mean(axis=0)).flatten()
    scored = list(zip(words, mean_tfidf))
    scored.sort(key=lambda x: x[1], reverse=True)
    scored = scored[:top_n]

    table = Table(title=f"Top {top_n} Palavras - TF-IDF Médio")
    table.add_column("Palavra", style="bold")
    table.add_column("TF-IDF Médio", justify="right")

    for word, score in scored:
        table.add_row(word, f"{score:.4f}")
    console.print(table)

def lda(texts, n_topics=2, n_words=3):
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(texts)
    lda_model = LatentDirichletAllocation(n_components=n_topics, random_state=42)
    lda_model.fit(X)
    feature_names = vectorizer.get_feature_names_out()

    console.print("\nTópicos (LDA):", style="bold underline")
    for idx, topic in enumerate(lda_model.components_):
        top_features_idx = topic.argsort()[-n_words:][::-1]
        top_features = [feature_names[i] for i in top_features_idx]
        console.print(f"[bold cyan]Tópico {idx + 1}:[/] {', '.join(top_features)}")
