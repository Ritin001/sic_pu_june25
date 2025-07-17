import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Path to cleaned data
CLEANED_DATA_PATH = r"C:\learning\sic_pu_june25\Hackathon\data\clean_data.csv"

# Prices for each sweet item
PRICE_DICT = {
    "angbutter": 4800,
    "plain bread": 3500,
    "jam": 1500,
    "ice coffe": 4000,
    "croissant": 3500,
    "ice coffe latter": 4500,
    "tiramisu croissant": 4800,
    "cacao deep": 4000,
    "pain au chocolat": 3500,
    "almond croissant": 4000,
    "ice milk tea": 4500,
    "gateau chocolat": 4000,
    "pandoro": 4500,
    "cheese cake": 5000,
    "lemon ade": 4500,
    "orange pound": 4500,
    "wiener": 2500,
    "valina latte": 4500,
    "berry ade": 4500,
    "tiramisu": 4500,
    "merinque cookies": 4000
}

def calculate_revenue(row):
    revenue = 0
    for item, price in PRICE_DICT.items():
        if item in row:
            revenue += row[item] * price
    return revenue

def plot_total_money_vs_day():
    df = pd.read_csv(CLEANED_DATA_PATH)

    # Calculate revenue for each row
    df['revenue'] = df.apply(calculate_revenue, axis=1)

    # Group by day and sum revenue
    grouped = df.groupby('day of week')['revenue'].sum().reindex([
        'Mon', 'Tue', 'Wed', 'Thur', 'Fri', 'Sat', 'Sun'
    ])

    # Create the plot
    plt.figure(figsize=(10, 6))
    sns.barplot(x=grouped.index, y=grouped.values, palette='pink')
    plt.title('Total Revenue by Day of Week (₹)', fontsize=14)
    plt.xlabel('Day of Week')
    plt.ylabel('Total Revenue (₹)')
    plt.tight_layout()
    fig = plt.gcf()

    # Generate insight
    max_day = grouped.idxmax()
    max_value = grouped.max()
    insight = f"The highest revenue was on {max_day} with ₹{max_value:,.0f}."

    return fig, insight

# For standalone testing
if __name__ == "__main__":
    fig, insight = plot_total_money_vs_day()
    print(insight)
    plt.show()
