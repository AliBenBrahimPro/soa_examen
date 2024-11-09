import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

nlp = spacy.load('en_core_web_md')

def load_data():
    # Load CV
    cv_file_path = "developer_cv.txt"
    with open(cv_file_path, 'r') as file:
        cv_text = file.read()

    # Load job descriptions
    job_file_path = "tech_job_descriptions.xlsx"
    job_df = pd.read_excel(job_file_path)
    job_descriptions = job_df["Job Description"].tolist()
    company_names = job_df["Company Name"].tolist()

    return cv_text, job_descriptions, company_names

def preprocess(text):
    doc = nlp(text.lower())
    return " ".join([token.lemma_ for token in doc if not token.is_stop and not token.is_punct])

def calculate_similarity(processed_cv, processed_jobs):
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([processed_cv] + processed_jobs)
    return cosine_similarity(vectors[0:1], vectors[1:]).flatten()

def calculate_similarity_partial(args):
    processed_cv, processed_job = args
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([processed_cv, processed_job])
    return cosine_similarity(vectors[0:1], vectors[1:2]).flatten()[0]
