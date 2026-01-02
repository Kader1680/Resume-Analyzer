from google.genai import Client
import os

client = Client(api_key=os.getenv("GEMINI_API_KEY"))

def analyse_resume_gemini(resume_content, job_description):
    prompt = f"""
    You are a professional resume analyzer.

    Resume:
    {resume_content}

    Job Description:
    {job_description}

    Task:
    - Analyze the resume against the job description.
    - Give a match score out of 100.
    - Highlight missing skills or experiences.
    - Suggest improvements.

    Return the result in structured format:
    Match Score: XX/100
    Missing Skills:
    - ...
    Suggestions:
    - ...
    Summary:
    ...
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",  
        contents=prompt
    )

    return response.text
