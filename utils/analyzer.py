import docx2txt
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def extract_text_from_docx(docx_file):
    return docx2txt.process(docx_file)

def calculate_match_score(cv_text, jd_text):
    corpus = [cv_text, jd_text]
    vectorizer = CountVectorizer()
    vectors = vectorizer.fit_transform(corpus)
    return cosine_similarity(vectors[0], vectors[1])[0][0]
