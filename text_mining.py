import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.decomposition import LatentDirichletAllocation

texts = [
    "O Brasil é o maior exportador de soja.",
    "A inflação no país tem subido nos últimos meses.",
    "O desemprego caiu, mas ainda preocupa."
]

def word_count():
    vectorizer = CountVectorizer()
    counts = vectorizer.fit_transform(texts)
    df = pd.DataFrame(counts.toarray(), columns=vectorizer.get_feature_names_out())
    print("\nContagem de palavras:")
    print(df)

def tfidf():
    vectorizer = TfidfVectorizer()
    tfidf = vectorizer.fit_transform(texts)
    df = pd.DataFrame(tfidf.toarray(), columns=vectorizer.get_feature_names_out())
    print("\nTF-IDF:")
    print(df)

def lda():
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(texts)
    lda = LatentDirichletAllocation(n_components=2, random_state=42)
    lda.fit(X)
    print("\nTópicos (LDA):")
    for idx, topic in enumerate(lda.components_):
        terms = [vectorizer.get_feature_names_out()[i] for i in topic.argsort()[-3:]]
        print(f"Tópico {idx+1}: {', '.join(terms)}")

if __name__ == "__main__":
    word_count()
    tfidf()
    lda()
