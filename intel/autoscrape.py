from autoscraper import AutoScraper
import pandas as pd

# Step 1: Define the Amazon product URL
amazon_url = "https://www.amazon.in/Intel-i7-12700K-Desktop-Processor-Unlocked/dp/B09FXNVDBJ"

# Step 2: Initialize Autoscraper
scraper = AutoScraper()
wanted_list = ["5.0 out of 5 stars", "Amazing Processor!", "Reviewed in India on January 1, 2023"]

# Step 3: Build the scraper
result = scraper.build(amazon_url, wanted_list)

# Step 4: Inspect the generated rules
grouped_results = scraper.get_result_similar(amazon_url, grouped=True)
print("Grouped Results:", grouped_results)

# Inspect the rules
rules = list(grouped_results.keys())
print("Generated Rules:", rules)

for rule in rules:
    print(f"Rule: {rule}, Output: {grouped_results[rule]}")

# Set the rule aliases based on inspected rules
# Example: If the inspected rules are different, adjust the keys below
scraper.set_rule_aliases({
    rules[0]: 'Rating',
    rules[1]: 'Review Title',
    rules[2]: 'Review Body',
    rules[3]: 'Review Date'
})

# Step 5: Keep only the relevant rules
scraper.keep_rules(rules[:4])  # Adjust according to the actual number of rules
scraper.save('amazon-reviews')

# Step 6: Load the scraper with saved rules
scraper.load('amazon-reviews')

# Step 7: Scrape all pages
def scrape_all_pages(base_url, page_limit=10):
    reviews = []
    for page in range(1, page_limit + 1):
        url = f"{base_url}?pageNumber={page}"
        page_results = scraper.get_result_similar(url, group_by_alias=True)
        reviews.append(page_results)
    return reviews

# Step 8: Extract reviews
reviews = scrape_all_pages(amazon_url, page_limit=10)

# Step 9: Filter reviews from 2022 to 2024
filtered_reviews = []
for review_page in reviews:
    for review in review_page:
        if 'Review Date' in review and any(year in review['Review Date'] for year in ['2022', '2023', '2024']):
            filtered_reviews.append(review)

# Step 10: Save to CSV
df = pd.DataFrame(filtered_reviews)
df.to_csv('amazon_reviews.csv', index=False)

print("Reviews have been successfully scraped and saved to 'amazon_reviews.csv'")
