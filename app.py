from utils import preprocess_text
from learning_engine import process_user_input
import recommendation_engine

def main():
    # Take user input
    user_query = input("Enter your query (job description or skills): ")

    # Preprocess user input
    normalized_query = preprocess_text(user_query)

    # Process user input to extract relevant skills
    relevant_skills = process_user_input(normalized_query)

    # Calculate similarity to recommend courses
    recommendation_engine.calculate_similarity(relevant_skills)

    return relevant_skills

if __name__ == "__main__":
    main()