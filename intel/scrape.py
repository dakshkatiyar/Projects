# hari aur khud ka full wla

import requests
from bs4 import BeautifulSoup
import pandas as pd
import random

reviewList = []

def extractReview(reviewUrl):
    headers = {"User-Agent": "Your User Agent"}
    resp = requests.get(reviewUrl, headers=headers)
    soup = BeautifulSoup(resp.text, 'html.parser')
    reviews = soup.findAll('div', {'data-hook': 'review'})
    for item in reviews:
        review_tag = item.find('a', {'data-hook': 'review-title'})
        review_title = review_tag.find_all('span')[-1].text.strip() 
        review = {
            'Review Title': review_title,
            'Rating': item.find('i', {'data-hook': 'review-star-rating'}).text.strip(),
            'Review Body': item.find('span', {'data-hook': 'review-body'}).text.strip(),
            'Review Date': item.find('span', {'data-hook': 'review-date'}).text.strip().split()[-2:]
        }
        reviewList.append(review)

def totalpage(reviewUrl):
    headers = {"User-Agent": "Your User Agent"}
    resp = requests.get(reviewUrl, headers=headers)
    soup = BeautifulSoup(resp.text, 'html.parser')
    num = soup.find('div', {'data-hook' : 'cr-filter-info-review-rating-count'})
    return 1+ int(num.text.strip().split(", ")[1].split(" ")[0])//10



url = "https://www.amazon.in/Redmi-Moonstone-Silver-128GB-Storage/dp/B0CDQ8P8S4/"
reviewUrl = url.replace("dp", "product-reviews") + f"?pageNumber={2}"+ "&sortBy=recent"
print(reviewUrl)

totalPage = totalpage(reviewUrl)
extractReview(reviewUrl)

for i in range(1, totalPage+1):
    try:
        print(f"running for page {i}")
        reviewUrl = url.replace("dp", "product-reviews") + f"?pageNumber={i}"+ "&sortBy=recent"
        extractReview(reviewUrl)
    except Exception as e:
        print(e) 


df = pd.DataFrame(reviewList)
df.to_csv("output.csv", index=False)