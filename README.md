# Recommender System

This is a recommender system that suggests relevant courses based on a user's input job description or desired skills. The system uses natural language processing and machine learning techniques to match the user's input with course content.


## Features

- Extracts relevant skills from the user's input job description or desired skills.
- Processes and tokenizes course descriptions from PDF files.
- Calculates the similarity between the user's input and course content using TF-IDF and cosine similarity.
- Recommends the top 10 most relevant courses to the user.

## Installation

1. Clone the repository:
  ```git clone https://github.com/notanshb/Recommender-System.git```

3. Install the required dependencies:
   ```pip install -r requirements.txt```


## Usage

1. Place the course PDF files in the `data/courses/cs` directory.
2. Run the `app.py` script:
   ```python app.py```
3. Enter your job description or desired skills when prompted.
4. The system will output the top 10 recommended courses based on your input.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request if you have any improvements or bug fixes.
