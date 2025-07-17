import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

CLEANED_DATA_PATH = r"C:\learning\sic_pu_june25\Hackathon\data\clean_data.csv"

def plot_total_quantity_vs_day():
    df = pd.read_csv(CLEANED_DATA_PATH)

    # Drop non-sweet columns
    exclude_columns = ['total', 'day of week']
    sweet_columns = [col for col in df.columns if col not in exclude_columns]

    # Sum all sweet quantities per row, then group by day
    df['total_quantity'] = df[sweet_columns].sum(axis=1)
    grouped = df.groupby('day of week')['total_quantity'].sum().reindex([
        'Mon', 'Tue', 'Wed', 'Thur', 'Fri', 'Sat', 'Sun'
    ])

    # Plot
    plt.figure(figsize=(10, 6))
    sns.barplot(x=grouped.index, y=grouped.values, palette='pink')
    plt.title('Total Quantity Sold by Day of Week', fontsize=14)
    plt.xlabel('Day of Week')
    plt.ylabel('Total Quantity')
    plt.tight_layout()
    fig = plt.gcf()

    # Insight
    max_day = grouped.idxmax()
    max_qty = grouped.max()
    insight = f"The highest quantity of sweets was sold on {max_day} ({int(max_qty)} units)."

    return fig, insight

# For testing
if __name__ == "__main__":
    fig, insight = plot_total_quantity_vs_day()
    print(insight)
    plt.show()
