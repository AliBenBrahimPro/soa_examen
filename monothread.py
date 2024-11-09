from tasks import load_data, preprocess, calculate_similarity

def run_monothread():
    cv_text, job_descriptions, company_names = load_data()
    processed_cv = preprocess(cv_text)
    processed_jobs = [preprocess(desc) for desc in job_descriptions]
    similarity_scores = calculate_similarity(processed_cv, processed_jobs)

    # Sort by similarity and display top 5 results
    sorted_indices = similarity_scores.argsort()[::-1]
    sorted_jobs = [(company_names[i], job_descriptions[i], similarity_scores[i]) for i in sorted_indices]
    
    print("Top 5 Job Descriptions (Monothread):")
    for i, (company, desc, score) in enumerate(sorted_jobs[:5], start=1):
        print(f"{i}. Company: {company}\n   Score: {score:.4f}\n   Description: {desc}\n")
