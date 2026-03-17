import streamlit as st
import pandas as pd

from parser import read_pdf, read_docx, extract_email, extract_phone, extract_name
from skills import extract_skills
from ranking import score_candidate


st.title("AI Resume Ranking System")


jd = st.text_area("Enter Job Description")


uploaded_files = st.file_uploader(
    "Upload Resumes",
    type=["pdf", "docx"],
    accept_multiple_files=True
)


data = []


if uploaded_files and jd:

    for file in uploaded_files:

        text = ""

        if file.name.endswith(".pdf"):
            text = read_pdf(file)

        elif file.name.endswith(".docx"):
            text = read_docx(file)


        name = extract_name(text)
        email = extract_email(text)
        phone = extract_phone(text)

        skills = extract_skills(text)

        jd_skills = extract_skills(jd)


        skill_match = len(set(skills) & set(jd_skills)) * 10


        exp = 5
        edu = 5
        loc = 5


        score = score_candidate(
            skill_match,
            exp,
            edu,
            loc
        )


        data.append(
            {
                "Name": name,
                "Email": email,
                "Skills": ", ".join(skills),
                "Score": score,
            }
        )


df = pd.DataFrame(data)

if not df.empty:

    df = df.sort_values(
        "Score",
        ascending=False
    )

    st.dataframe(df)