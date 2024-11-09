from tasks import load_data, preprocess, calculate_similarity_partial
from threading import Thread, Lock

def run_multithread():
    # Load data
    cv_text, job_descriptions, company_names = load_data()
    processed_cv = preprocess(cv_text)
    
    results = []  # To store results as tuples (company, job description, score)
    threads = []
    lock = Lock()  # Lock to manage concurrent access to results list
    
    def calculate_and_store_result(job_desc, company):
        processed_job = preprocess(job_desc)
        score = calculate_similarity_partial((processed_cv, processed_job))  # Pass both arguments as a tuple
        
        with lock:  # Ensure thread-safe append
            results.append((company, job_desc, score))

    # Start a thread for each job description
    for desc, company in zip(job_descriptions, company_names):
        thread = Thread(target=calculate_and_store_result, args=(desc, company))
        threads.append(thread)
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    # Sort results by score in descending order
    results.sort(key=lambda x: x[2], reverse=True)

    # Display top 5 job descriptions with the highest similarity score
    print("Top 5 Job Descriptions (Multithread):")
    for i, (company, desc, score) in enumerate(results[:5], start=1):
        print(f"{i}. Company: {company}\n   Score: {score:.4f}\n   Description: {desc}\n")


