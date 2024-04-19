# text_preprocessing.py
import re
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

# Ensure necessary NLTK data is downloaded
nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)
nltk.download('averaged_perceptron_tagger', quiet=True)

def remove_punctuation_and_capitalization(text):
    # Remove punctuation and convert to lowercase
    return re.sub(r'[^\w\s]', '', text).lower()

def remove_non_alpha(tokens):
    # Remove non-alphabetical tokens
    return [word for word in tokens if word.isalpha()]

def remove_stopwords_and_non_keywords(tokens, additional_non_keywords=set()):
    # Remove stop words and additional non-keywords
    stop_words = set(stopwords.words("english"))
    tokens = [word for word in tokens if word not in stop_words and word not in additional_non_keywords]
    return tokens

def lemmatize_tokens(tokens):
    # Lemmatize tokens
    lemmatizer = WordNetLemmatizer()
    return [lemmatizer.lemmatize(word) for word in tokens]

# New function to process tokens directly, to be used in utils.py
def process_tokens(tokens, additional_non_keywords=set()):
    tokens = remove_non_alpha(tokens)
    tokens = remove_stopwords_and_non_keywords(tokens, additional_non_keywords)
    tokens = lemmatize_tokens(tokens)
    return tokens
