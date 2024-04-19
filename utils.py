# utils.py
import os
import PyPDF2
import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag
from text_preprocessing import process_tokens

def process_pdf_to_keywords(input_pdf, output_folder, additional_non_keywords):
    with open(input_pdf, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        text = ""

        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text() if page.extract_text() else ''

    tokens = word_tokenize(text)
    tokens = process_tokens(tokens, additional_non_keywords)
    tagged_tokens = pos_tag(tokens)
    tokens = [word for word, pos in tagged_tokens if pos != 'NNP']

    output_filename = os.path.splitext(os.path.basename(input_pdf))[0] + "_EXTRACTED.txt"
    output_filepath = os.path.join(output_folder, output_filename)

    with open(output_filepath, 'w') as output_file:
        output_file.write(" ".join(tokens))

def process_pdfs_in_folder(folder_path, output_folder, additional_non_keywords=set()):
    os.makedirs(output_folder, exist_ok=True)
    for filename in os.listdir(folder_path):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(folder_path, filename)
            process_pdf_to_keywords(pdf_path, output_folder, additional_non_keywords)
