import pandas as pd
import matplotlib.pyplot as plt
import os

# Create the "graphs" folder if it doesn't exist
output_folder = "graphs"
os.makedirs(output_folder, exist_ok=True)

# Initialize lists to hold the data for each product
product_names = []
positive_counts = []
negative_counts = []
neutral_counts = []
competition_counts = []
future_expectations_counts = []

# Loop through all sentiment files in the "data 2" folder
input_folder = "data 2"
for filename in os.listdir(input_folder):
    if filename.endswith("_with_sentiment.csv"):
        # Extract the product name
        product_name = filename.split("_with_sentiment.csv")[0]
        product_names.append(product_name)

        # Load the sentiment data
        filepath = os.path.join(input_folder, filename)
        df = pd.read_csv(filepath)

        # Count the sentiment occurrences
        positive_count = df[df['Sentiment'] == 'Positive'].shape[0]
        negative_count = df[df['Sentiment'] == 'Negative'].shape[0]
        neutral_count = df[df['Sentiment'] == 'Neutral'].shape[0]
        competition_count = df[df['Sentiment'] == 'Competition Sentiment'].shape[0]
        future_expectations_count = df[df['Sentiment'] == 'Future Expectations'].shape[0]

        positive_counts.append(positive_count)
        negative_counts.append(negative_count)
        neutral_counts.append(neutral_count)
        competition_counts.append(competition_count)
        future_expectations_counts.append(future_expectations_count)

        # Create a new figure for each product
        fig, ax = plt.subplots(1, 2, figsize=(16, 8))

        # Plot the pie chart for positive, negative, and neutral sentiments
        labels = ['Positive', 'Negative', 'Neutral']
        sizes = [positive_count, negative_count, neutral_count]
        colors = ['#99ff99', '#ff6666', '#66b3ff']
        explode = (0.1, 0, 0)  # explode the first slice

        ax[0].pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%',
                  shadow=True, startangle=140)
        ax[0].axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        ax[0].set_title(f'Sentiment Distribution for {product_name}')

        # Plot the bar graph for sentiment counts
        categories = ['Positive', 'Negative', 'Neutral', 'Competition', 'Future Expectations']
        counts = [positive_count, negative_count, neutral_count, competition_count, future_expectations_count]
        bar_colors = ['#99ff99', '#ff6666', '#66b3ff', '#ffcc99', '#99ff99']

        ax[1].bar(categories, counts, color=bar_colors)
        ax[1].set_xlabel('Sentiment Categories')
        ax[1].set_ylabel('Counts')
        ax[1].set_title(f'Sentiment Counts for {product_name}')

        # Save the figure
        fig.suptitle(f'Sentiment Analysis for {product_name}', fontsize=16)
        plt.tight_layout(rect=[0, 0, 1, 0.96])
        plt.savefig(os.path.join(output_folder, f'{product_name}_sentiment_analysis.png'))
        plt.close()

print(f"Graphs have been generated and saved in the {output_folder} folder.")
