import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime
import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configure Selenium
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run in headless mode (without opening a browser window)
options.add_argument(f"user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{random.randint(70, 99)}.0.4472.124 Safari/537.36")
driver = webdriver.Chrome(options=options)

reviewList = []

def extractReview(reviewUrl):
    try:
        driver.get(reviewUrl)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div[data-hook="review"]')))
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        reviews = soup.findAll('div', {'data-hook': 'review'})
        print(f"Extracting reviews from URL: {reviewUrl}, found {len(reviews)} reviews")
        for item in reviews:
            review_tag = item.find('a', {'data-hook': 'review-title'})
            review_title = review_tag.find_all('span')[-1].text.strip() if review_tag else "No title"
            rating_tag = item.find('i', {'data-hook': 'review-star-rating'})
            rating = rating_tag.text.strip() if rating_tag else "No rating"
            review_body_tag = item.find('span', {'data-hook': 'review-body'})
            review_body = review_body_tag.text.strip() if review_body_tag else "No review body"
            review_date_tag = item.find('span', {'data-hook': 'review-date'})
            review_date_text = review_date_tag.text.strip() if review_date_tag else "No review date"
            
            # Extract the date and filter reviews from 2022 to 2024
            review_date = ' '.join(review_date_text.split()[-3:]) if review_date_tag else "No review date"
            try:
                review_date_parsed = datetime.strptime(review_date, '%d %B %Y')
                if review_date_parsed.year < 2022 or review_date_parsed.year > 2024:
                    continue
            except ValueError:
                continue

            review = {
                'Review Title': review_title,
                'Rating': rating,
                'Review Body': review_body,
                'Review Date': review_date
            }
            print(f"Appending review: {review}")
            reviewList.append(review)
    except Exception as e:
        # Save a screenshot for debugging
        driver.save_screenshot(f"error_page_{reviewUrl.split('=')[-2]}.png")
        print(f"Error on page {reviewUrl}: {e}")

# Main function to extract reviews
def main():
    base_url = "https://www.amazon.in/Intel-i7-12700K-Desktop-Processor-Unlocked/dp/B09FXNVDBJ"
    review_url = f"{base_url}?sortBy=recent"
    extractReview(review_url)

    # Write reviews to CSV
    keys = reviewList[0].keys()
    with open('reviews.csv', 'w', newline='', encoding='utf-8') as output_file:
        dict_writer = csv.DictWriter(output_file, fieldnames=keys)
        dict_writer.writeheader()
        dict_writer.writerows(sorted(reviewList, key=lambda x: datetime.strptime(x['Review Date'], '%d %B %Y'), reverse=True))

    driver.quit()

if __name__ == "__main__":
    main()
