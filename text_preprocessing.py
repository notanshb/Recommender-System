import os
import pdfplumber
import fitz 
from utils import preprocess_text
from PyPDF2 import PdfReader

def process_pdf_to_keywords(input_pdf, output_folder, encoding='utf-8'):
    text = ""
    with fitz.open(input_pdf) as doc:
        for page in doc:
            text += page.get_text()

    tokens = preprocess_text(text)
    output_filename = os.path.splitext(os.path.basename(input_pdf))[0] + "_token.txt"
    output_filepath = os.path.join(output_folder, output_filename)

    with open(output_filepath, 'w', encoding=encoding) as output_file:
        output_file.write(" ".join(tokens))

    return output_filepath

def process_pdfs_in_folder(folder_path, output_folder, encoding='utf-8'):
    os.makedirs(output_folder, exist_ok=True)
    token_files = []
    for filename in os.listdir(folder_path):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(folder_path, filename)
            token_file = process_pdf_to_keywords(pdf_path, output_folder, encoding)
            token_files.append(token_file)

    return token_files
