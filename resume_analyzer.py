from PyPDF2 import PdfReader

inputTextDescrpition = input("Enter Your Job Description: ")

reader = PdfReader("resume.pdf")
number_of_pages = len(reader.pages)

def extract_text_from_pdf():
    text = ""
    for page in reader.pages:  # <-- FIXED HERE
        text += page.extract_text()
    return text

resume_text = extract_text_from_pdf()

print("\n--- Resume Text ---")
print(resume_text[:500])  # first 500 characters only

print("\n--- Job Description ---")
print(inputTextDescrpition[:500])

import re

def get_keywords(text):
    text = text.lower()
    
    # 2. Remove punctuation using regex
    text = re.sub(r'[^a-z\s]', '', text)
    
    words = text.split()
    
    return set(words)
print(get_keywords(resume_text))
print(get_keywords(inputTextDescrpition))


def level_match(resume, description):
    resume_text = get_keywords(resume_text)
    descipption_text = get_keywords(inputTextDescrpition)
    match = descipption_text.intersection(resume_text)

    match = description_keywords.intersection(resume_keywords)
    match_percent = len(match) / len(description_keywords) * 100

    print(f"\ Match Score: {match_percent:.2f}%")
    print(f"  Matched Keywords: {', '.join(match)}")



level_match(resume_text, inputTextDescrpition)
























