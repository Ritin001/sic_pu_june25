import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Use relative path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CLEANED_DATA_PATH = os.path.join(BASE_DIR, '..', 'data', 'clean_data.csv')

def plot_top5_sweets():
    df = pd.read_csv(CLEANED_DATA_PATH)

    # Drop non-sweet columns
    non_sweet_columns = ['total', 'day of week']
    sweet_columns = [col for col in df.columns if col not in non_sweet_columns]

    # Sum total for each sweet
    total_sold = df[sweet_columns].sum().sort_values(ascending=False).head(5)

    # Plot
    plt.figure(figsize=(10, 6))
    sns.barplot(x=total_sold.values, y=total_sold.index, palette='pink')
    plt.title('Top 5 Selling Sweets', fontsize=14)
    plt.xlabel('Units Sold')
    plt.ylabel('Sweet Item')
    plt.tight_layout()
    fig = plt.gcf()

    # Insight
    top_item = total_sold.index[0]
    top_qty = total_sold.iloc[0]
    insight = f"The top-selling sweet is {top_item} with {int(top_qty)} units sold. This sweet is highly popular and should always be in stock."

    return fig, insight

# For testing
if __name__ == "__main__":
    fig, insight = plot_top5_sweets()
    print(insight)
    plt.show()
