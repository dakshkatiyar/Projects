from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

obj = SentimentIntensityAnalyzer()

line = "Bahut kharab phone software problem bahut hai"
sentiment_dict = obj.polarity_scores(line)
print(sentiment_dict)