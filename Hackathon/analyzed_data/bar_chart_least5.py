import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

CLEANED_DATA_PATH = r"C:\learning\sic_pu_june25\Hackathon\data\clean_data.csv"

def plot_least5_sweets():
    df = pd.read_csv(CLEANED_DATA_PATH)

    # Drop non-sweet columns
    non_sweet_columns = ['total', 'day of week']
    sweet_columns = [col for col in df.columns if col not in non_sweet_columns]

    # Sum total for each sweet and get least 5
    total_sold = df[sweet_columns].sum().sort_values(ascending=True).head(5)

    # Plot
    plt.figure(figsize=(10, 6))
    sns.barplot(x=total_sold.values, y=total_sold.index, palette='pink')
    plt.title('Least 5 Selling Sweets', fontsize=14)
    plt.xlabel('Units Sold')
    plt.ylabel('Sweet Item')
    plt.tight_layout()
    fig = plt.gcf()

    # Insight
    least_item = total_sold.index[0]
    least_qty = total_sold.iloc[0]
    insight = f"The least sold sweet is {least_item} with only {int(least_qty)} units sold."

    return fig, insight

# For testing
if __name__ == "__main__":
    fig, insight = plot_least5_sweets()
    print(insight)
    plt.show()
