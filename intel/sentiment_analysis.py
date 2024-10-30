import requests
from bs4 import BeautifulSoup
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt
import seaborn as sns

# Function to scrape reviews from Amazon
def get_amazon_reviews(url):
    headers = {"User-Agent": "Your User Agent"}
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    reviews = []
    for review in soup.find_all('span', {'data-hook': 'review-body'}):
        reviews.append(review.get_text().strip())
    return reviews

# Example URL (replace with actual product review URL)
url = 'https://www.amazon.com/product-reviews/B08T6F9HS2'
reviews = get_amazon_reviews(url)

# Initialize VADER sentiment analyzer
analyzer = SentimentIntensityAnalyzer()

# Analyze sentiment for each review
sentiment_scores = [analyzer.polarity_scores(review)['compound'] for review in reviews]

# Print each review with its sentiment score
for review, score in zip(reviews, sentiment_scores):
    print(f"Review: {review}\nScore: {score}\n")

# Visualize the sentiment scores
sns.histplot(sentiment_scores, kde=True)
plt.title('Distribution of Sentiment Scores')
plt.xlabel('Sentiment Score')
plt.ylabel('Frequency')
plt.show()
