import pandas as pd
import matplotlib.pyplot as plt
import os

# Use relative path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CLEANED_DATA_PATH = os.path.join(BASE_DIR, '..', 'data', 'clean_data.csv')

def plot_pie_chart_for_weekday(weekday):
    df = pd.read_csv(CLEANED_DATA_PATH)

    # Drop non-sweet columns
    non_sweets = ['day of week', 'total', 'revenue']
    sweet_columns = [col for col in df.columns if col not in non_sweets]

    # Filter for selected weekday
    weekday_df = df[df['day of week'] == weekday]

    if weekday_df.empty:
        print(f"❌ No data found for {weekday}")
        return None

    # Sum sweet quantities
    sweet_totals = weekday_df[sweet_columns].sum()
    sweet_totals = sweet_totals[sweet_totals > 0]  # Remove 0-sales sweets

    # Plot pie chart
    plt.figure(figsize=(8, 8))
    plt.pie(
        sweet_totals.values,
        labels=sweet_totals.index,
        autopct='%1.1f%%',
        startangle=140,
        colors=plt.cm.Set3.colors
    )
    plt.title(f"Sweet Sales Distribution on {weekday}")
    plt.tight_layout()

    return plt.gcf()

# Standalone test mode
if __name__ == "__main__":
    df = pd.read_csv(CLEANED_DATA_PATH)
    weekdays = sorted(df['day of week'].unique())
    
    print("📅 Available weekdays in data:")
    for day in weekdays:
        print(f" - {day}")

    selected_day = input("\nEnter one of the above weekdays: ").strip()

    fig = plot_pie_chart_for_weekday(selected_day)
    if fig:
        plt.show()
