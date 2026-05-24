import pandas as pd
import nltk
from nltk.corpus import stopwords
import string

# Load the reviews dataset
df = pd.read_csv("data/TestReviews.csv")

# Downloads the stopwords
nltk.download('stopwords')

# Load the english stopwords set
stop_words = set(stopwords.words('english'))

def review_cleaning(text):
    removed_punctuations = text.translate(str.maketrans(" ", " ", string.punctuation))
    reviews = removed_punctuations.split()
    filtered_reviews = [review.lower() for review in reviews if review.lower() not in stop_words]
    return ", ".join(filtered_reviews)

df['cleaned_review'] = df['review'].apply(review_cleaning)

df['cleaned_review'].to_csv('data/cleaned_reviews.csv', index=False)

tokenize_review = pd.read_csv("data/cleaned_reviews.csv")
print(tokenize_review.head())