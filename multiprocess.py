from tasks import load_data, preprocess, calculate_similarity_partial
from multiprocessing import Pool

def run_multiprocess():
    cv_text, job_descriptions, company_names = load_data()
    processed_cv = preprocess(cv_text)
    
    with Pool() as pool:
        processed_jobs = pool.map(preprocess, job_descriptions)
        similarity_scores = pool.map(calculate_similarity_partial, [(processed_cv, job) for job in processed_jobs])

    # Sort and display top 5 results
    sorted_indices = sorted(range(len(similarity_scores)), key=lambda k: similarity_scores[k], reverse=True)
    sorted_jobs = [(company_names[i], job_descriptions[i], similarity_scores[i]) for i in sorted_indices]

    print("Top 5 Job Descriptions (Multiprocess):")
    for i, (company, desc, score) in enumerate(sorted_jobs[:5], start=1):
        print(f"{i}. Company: {company}\n   Score: {score:.4f}\n   Description: {desc}\n")
