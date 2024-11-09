import pandas as pd
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import time

# Measure execution time
start_time = time.time()

# Load the CV text
cv_file_path = "developer_cv.txt"
with open(cv_file_path, 'r') as file:
    cv_text = file.read()

# Load job descriptions from the Excel file
job_file_path = "tech_job_descriptions.xlsx"
job_df = pd.read_excel(job_file_path)
job_descriptions = job_df["Job Description"].tolist()
company_names = job_df["Company Name"].tolist()

# Load pre-trained spaCy model
nlp = spacy.load('en_core_web_md')

# Text preprocessing function
def preprocess(text):
    """Preprocesses text by lowercasing and lemmatizing using spaCy."""
    doc = nlp(text.lower())
    return " ".join([token.lemma_ for token in doc if not token.is_stop and not token.is_punct])

# Preprocess the CV and job descriptions
processed_cv = preprocess(cv_text)
processed_jobs = [preprocess(desc) for desc in job_descriptions]

# TF-IDF Vectorization
vectorizer = TfidfVectorizer()
vectors = vectorizer.fit_transform([processed_cv] + processed_jobs)

# Calculate similarity scores
similarity_scores = cosine_similarity(vectors[0:1], vectors[1:]).flatten()

# Sort job descriptions by similarity score
sorted_indices = similarity_scores.argsort()[::-1]
sorted_jobs = [(company_names[i], job_descriptions[i], similarity_scores[i]) for i in sorted_indices]

# Execution time
execution_time = time.time() - start_time

# Display results
print("Top 10 Job Descriptions ranked by relevance (Company Name included):")
for i, (company, desc, score) in enumerate(sorted_jobs[:5], start=1):  # Show top 10 matches
    print(f"{i}. Company: {company}\n   Score: {score:.4f}\n   Description: {desc}\n")

print(f"Execution Time: {execution_time:.4f} seconds")
