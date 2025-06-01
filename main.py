# Import required libraries
import fitz  # PyMuPDF
import re
import spacy

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# ---- Text Extraction ----
def extract_text_from_pdf(path):
    doc = fitz.open(path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

# ---- Info Extraction ----
def extract_email(text):
    match = re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", text)
    return match[0] if match else "Not found"

def extract_phone(text):
    match = re.findall(r"\+?\d[\d -]{8,12}\d", text)
    return match[0] if match else "Not found"

def extract_university(text):
    # Common phrases around university names in resumes
    university_keywords = ["university", "college", "institute", "academy", "school"]
    text = text.lower()
    for keyword in university_keywords:
        if keyword in text:
            # Extract the line containing university name
            lines = text.split('\n')
            for line in lines:
                if keyword in line:
                    return line.strip()
    return "Not found"

# ---- Skill Extraction (Using skills.txt) ----
def extract_skills(text, skills_file='skills.txt'):
    with open(skills_file, 'r') as f:
        skillset = [line.strip() for line in f.readlines()]

    found_skills = []
    text = text.lower()
    for skill in skillset:
        if skill.lower() in text:
            found_skills.append(skill)
    return list(set(found_skills))

# ---- Main Execution ----
resume_path = "resume.pdf"  # Upload your resume file before running
text = extract_text_from_pdf(resume_path)

print("=== Resume Info ===")
print("Email:", extract_email(text))
print("Phone:", extract_phone(text))
print("University:", extract_university(text))
print("Skills:", ", ".join(extract_skills(text)))
