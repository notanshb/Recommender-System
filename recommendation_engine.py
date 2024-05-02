import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from learning_engine import process_user_input
from text_preprocessing import process_pdfs_in_folder
from utils import preprocess_text

def calculate_similarity(relevant_skills):
    # Preprocess the user query
    normalized_query = preprocess_text(relevant_skills)

    # Calculate TF-IDF vectors for relevant_skills and each token file
    vectorizer = TfidfVectorizer()
    token_files = process_pdfs_in_folder('data/courses/cs', 'data/token_files')
    token_texts = []

    for file_path in token_files:
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                token_texts.append(file.read())
        except UnicodeDecodeError:
            print(f"Error decoding file: {file_path}. Skipping.")

    tfidf_matrix = vectorizer.fit_transform([relevant_skills] + token_texts)

    # Calculate cosine similarity between relevant_skills and each token file
    cosine_similarities = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:])[0]

    # Get the top 10 most similar token files
    top_indexes = cosine_similarities.argsort()[-10:][::-1]
    top_token_files = [token_files[i] for i in top_indexes]

    # Output the corresponding PDF file names
    print("Top 10 recommended courses :")
    for file in top_token_files:
        pdf_name = os.path.splitext(os.path.basename(file))[0].replace("_token", "")
        print(pdf_name)