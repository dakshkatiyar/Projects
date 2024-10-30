import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_amazon_reviews(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    
    reviews = []
    for review in soup.select(".review"):
        review_title = review.select_one(".review-title").get_text(strip=True)
        review_text = review.select_one(".review-text-content").get_text(strip=True)
        reviews.append({"title": review_title, "text": review_text})
    
    return reviews

url = "https://www.amazon.com/product-reviews/B08P5YQ7QJ"  # Example product URL
reviews = get_amazon_reviews(url)

# Save reviews to a CSV file
df = pd.DataFrame(reviews)
df.to_csv("amazon_reviews.csv", index=False)
