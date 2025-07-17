import pandas as pd

# Use absolute paths
RAW_DATA_PATH = r"C:\learning\sic_pu_june25\Hackathon\data\raw_data.csv"
CLEANED_DATA_PATH = r"C:\learning\sic_pu_june25\Hackathon\data\clean_data.csv"

def clean_kanti_data():
    try:
        # Step 1: Load the raw CSV
        df = pd.read_csv(RAW_DATA_PATH)

        # Step 2: Drop unwanted columns
        df.drop(columns=['datetime', 'place'], inplace=True, errors='ignore')

        # Step 3: Replace all empty or missing values with 0
        df.replace('', 0, inplace=True)   # Replace blank strings
        df.fillna(0, inplace=True)        # Replace NaNs

        # Step 4: Convert all numeric columns (except 'day of week') to integers
        for col in df.columns:
            if col != 'day of week':
                df[col] = df[col].astype(int)

        # Step 5: Save cleaned data
        df.to_csv(CLEANED_DATA_PATH, index=False)
        print(f"✅ Cleaned data saved to: {CLEANED_DATA_PATH}")

    except Exception as e:
        print(f"❌ Error during cleaning: {e}")

if __name__ == "__main__":
    clean_kanti_data()
