from text_preprocessing import preprocess_query
from learning_engine import extract_skills
from recommendation_engine import recommend_courses

def main():
    user_query = input("Enter your query (job description or skills): ")
    normalized_query = preprocess_query(user_query)
    relevant_skills = extract_skills(normalized_query)
    recommended_courses = recommend_courses(relevant_skills)
    print("Recommended Courses:", recommended_courses)

if __name__ == "__main__":
    main()


# app.py when i made utils.py to have course pdf to keyword conversion functionality
# from utils import process_pdfs_in_folder

# def main():
#     pdf_folder_path = 'data/courses/CS'  # Adjust this path to your source folder
#     output_folder_path = 'data/course_keywords'  # Adjust this path for the output folder

#     # Define additional non-keywords if needed
#     additional_non_keywords = set(['example_non_keyword1', 'example_non_keyword2'])

#     process_pdfs_in_folder(pdf_folder_path, output_folder_path, additional_non_keywords)
#     print("PDF processing complete. Keywords extracted to:", output_folder_path)

# if __name__ == "__main__":
#     main()
