import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

CLEANED_DATA_PATH = r"C:\learning\sic_pu_june25\Hackathon\data\clean_data.csv"

def plot_heatmap_for_weekdays(selected_days):
    df = pd.read_csv(CLEANED_DATA_PATH)

    # Drop non-sweet columns
    non_sweets = ['day of week', 'total', 'revenue']
    sweet_columns = [col for col in df.columns if col not in non_sweets]

    # Filter data for selected weekdays
    df_filtered = df[df['day of week'].isin(selected_days)]

    if df_filtered.empty:
        print("❌ No data for selected weekdays.")
        return None

    # Group by 'day of week' and sum sweet quantities
    heatmap_data = df_filtered.groupby('day of week')[sweet_columns].sum()

    # Reorder the days as per user input
    heatmap_data = heatmap_data.reindex(selected_days)

    # Plot heatmap
    plt.figure(figsize=(12, 6))
    sns.heatmap(heatmap_data, cmap="YlOrRd", annot=True, fmt='d')
    plt.title("Sweet Sales Heatmap for Selected Weekdays")
    plt.xlabel("Sweets")
    plt.ylabel("Day of Week")
    plt.xticks(rotation=45)
    plt.tight_layout()

    return plt.gcf()

# For standalone testing
if __name__ == "__main__":
    df = pd.read_csv(CLEANED_DATA_PATH)
    weekdays = sorted(df['day of week'].unique())

    print("📅 Available weekdays:", ", ".join(weekdays))
    selected_days_input = input("Enter weekdays (comma-separated, e.g., Mon,Fri,Sat): ").strip()
    selected_days = [day.strip() for day in selected_days_input.split(",") if day.strip() in weekdays]

    if not selected_days:
        print("❌ No valid weekdays entered.")
    else:
        fig = plot_heatmap_for_weekdays(selected_days)
        if fig:
            plt.show()
