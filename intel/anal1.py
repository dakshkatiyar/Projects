import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import ssl
import nltk
import os

# Bypass SSL certificate check
try:
    _create_unverified_https_context = ssl._create_unverified_https_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

# Download the vader_lexicon resource
nltk.download('vader_lexicon')

# Initialize Vader Sentiment Analyzer
sia = SentimentIntensityAnalyzer()

# Function to classify sentiment
def classify_sentiment(text):
    vader_score = sia.polarity_scores(text)['compound']
    if vader_score >= 0.05:
        return 'Positive'
    elif vader_score <= -0.05:
        return 'Negative'
    else:
        return 'Neutral'

# Function to identify competition sentiment and future expectations
def identify_special_sentiment(text):
    competitors = ["amd", "apple", "qualcomm", "arm", "nvidia", "ibm", "samsung", "mediatek"]
    if any(word in text.lower() for word in ["competitor", "competition", "rival"] + competitors):
        return 'Competition Sentiment'
    if any(word in text.lower() for word in ["expect", "hope", "future", "wish"]):
        return 'Future Expectations'
    return classify_sentiment(text)

# Create output folder if it doesn't exist
output_folder = "data 2"
os.makedirs(output_folder, exist_ok=True)

# Loop through all CSV files in the input folder
input_folder = "data"
for filename in os.listdir(input_folder):
    if filename.endswith(".csv"):
        # Load the CSV file
        filepath = os.path.join(input_folder, filename)
        df = pd.read_csv(filepath)

        # Convert non-string entries to strings and fill missing values
        df['Review Body'] = df['Review Body'].astype(str).fillna('')

        # Apply the sentiment identification function to the dataframe
        df['Sentiment'] = df['Review Body'].apply(identify_special_sentiment)

        # Save the complete dataframe with sentiment analysis
        output_filepath = os.path.join(output_folder, f"{filename.split('.')[0]}_with_sentiment.csv")
        df.to_csv(output_filepath, index=False)

        print(f"Sentiment analysis completed for {filename} and saved to the {output_folder} folder.")
