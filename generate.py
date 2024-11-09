import pandas as pd
import random

# Generate random company names and locations
def generate_company_name():
    prefixes = ["Tech", "Code", "Data", "AI", "Soft", "Info"]
    suffixes = ["Nova", "Sphere", "Dynamics", "Labs", "Solutions", "Works"]
    return f"{random.choice(prefixes)}{random.choice(suffixes)}"

def generate_location():
    cities = ["San Francisco", "New York", "London", "Berlin", "Tokyo", "Sydney", "Toronto", "Dubai", "Singapore", "Paris"]
    return random.choice(cities)

# Frameworks and corresponding job titles
frameworks = {
    "Python": ["Django Developer", "Flask Engineer", "TensorFlow Specialist", "Data Scientist (pandas)"],
    "JavaScript": ["React Developer", "Angular Engineer", "Vue.js Frontend Developer", "Node.js Backend Developer"],
    "Java": ["Spring Developer", "Android Developer", "Big Data Engineer (Hadoop)"],
    "C++": ["Qt Developer", "Game Developer (Unreal Engine)", "IoT Developer (Arduino)"],
    "C#": [".NET Developer", "Unity Game Developer", "Mobile Developer (Xamarin)"],
    "PHP": ["Laravel Developer", "WordPress Engineer", "Symfony Developer"]
}

# Sample descriptions and salary ranges
descriptions = {
    "Python": "Develop scalable applications and work on data-intensive projects using {framework}.",
    "JavaScript": "Build dynamic web applications and user interfaces using {framework}.",
    "Java": "Create robust enterprise solutions and mobile applications using {framework}.",
    "C++": "Design high-performance systems and applications using {framework}.",
    "C#": "Develop cross-platform solutions and games using {framework}.",
    "PHP": "Develop efficient web applications and CMS platforms using {framework}."
}
salary_ranges = ["$70,000 - $90,000", "$90,000 - $110,000", "$110,000 - $130,000"]

# Generate 100 rows
data = []
job_id = 1
for language, job_titles in frameworks.items():
    for framework in job_titles:
        data.append({
            "Job ID": f"JOB{job_id:03}",
            "Company Name": generate_company_name(),
            "Job Title": framework,
            "Job Description": descriptions[language].format(framework=framework),
            "Required Skills": f"{language}, {framework}",
            "Location": generate_location(),
            "Salary Range": random.choice(salary_ranges)
        })
        job_id += 1

# Convert to DataFrame and save as Excel
df = pd.DataFrame(data)
file_path = "tech_job_descriptions_with_names.xlsx"
df.to_excel(file_path, index=False)
print(f"Excel file saved at: {file_path}")