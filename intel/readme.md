# Intel Products Sentiment Analysis from Online Reviews

## Problem Statement

Analyzing customer sentiment from online reviews of Intel products to understand customer satisfaction and areas of improvement.

## Unique Idea Brief (Solution)

This project employs web scraping and sentiment analysis techniques to extract and analyze reviews from various online sources. Using VaderSentiment, the analysis classifies reviews into positive, negative, and neutral categories, providing a comprehensive understanding of customer sentiment towards Intel products.

## Features Offered

- **Web Scraping**: Extract reviews from multiple online platforms.
- **Sentiment Analysis**: Classify reviews using VaderSentiment.
- **Data Visualization**: Visualize sentiment distribution and trends.
- **CSV Export**: Export sentiment analysis results to CSV files.

## Process Flow

1. **Scraping Reviews**: Collect reviews from online sources.
2. **Data Preprocessing**: Clean and organize the scraped data.
3. **Sentiment Analysis**: Analyze the sentiment of each review using VaderSentiment.
4. **Data Visualization**: Create graphs and charts to visualize the results.
5. **Export Results**: Save the results to CSV files for further analysis.

## Architecture Diagram

```plaintext
    +--------------------+
    |  Scrape Reviews    |
    +---------+----------+
              |
              v
    +---------+----------+
    |  Data Preprocessing |
    +---------+----------+
              |
              v
    +---------+----------+
    |  Sentiment Analysis |
    +---------+----------+
              |
              v
    +---------+----------+
    |  Data Visualization |
    +---------+----------+
              |
              v
    +---------+----------+
    |   Export Results   |
    +--------------------+
```

## Technologies Used

- **Python**
- **Beautiful Soup**: For web scraping
- **VaderSentiment**: For sentiment analysis
- **Matplotlib**: For data visualization
- **Pandas**: For data manipulation

## Team Members and Contributions

- **Prity Mishra**: Scraping, preprocessing, and management.
- **Daksh Katiyar**: Analysis, visualization, and conclusions.

## Conclusion

This project provides a comprehensive solution for analyzing customer sentiment from online reviews of Intel products. By leveraging web scraping, sentiment analysis, and data visualization, we offer valuable insights into customer opinions, helping Intel improve its products and services based on real user feedback.