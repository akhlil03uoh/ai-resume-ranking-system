import pdfplumber
import docx
import re


def read_pdf(file):
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + " "
    return text


def read_docx(file):
    doc = docx.Document(file)
    text = ""
    for para in doc.paragraphs:
        text += para.text + " "
    return text


def extract_email(text):
    match = re.findall(r'\S+@\S+', text)
    return match[0] if match else ""


def extract_phone(text):
    match = re.findall(r'\d{10}', text)
    return match[0] if match else ""


def extract_name(text):
    lines = text.split("\n")
    return lines[0]