import pandas as pd
import matplotlib

# ✅ Force backend (VERY IMPORTANT FIX)
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import os

def main():

    # -----------------------------
    # 1. LOAD DATA
    # -----------------------------
    dataset_path = "LPG_Impact_Jan_Mar_2026_Realistic.xlsx"
    df = pd.read_excel(dataset_path)

    print("✅ Dataset Loaded Successfully\n")
    print(df.head())

    # -----------------------------
    # 2. DATA CLEANING
    # -----------------------------
    df['Date'] = pd.to_datetime(df['Date'])
    df = df.sort_values(by='Date')

    # -----------------------------
    # CREATE OUTPUT FOLDER
    # -----------------------------
    output_folder = "graphs"
    os.makedirs(output_folder, exist_ok=True)

    # -----------------------------
    # 3. LPG PRICE TREND
    # -----------------------------
    plt.figure()
    df.groupby('Date')['LPG_Price'].mean().plot(marker='o')
    plt.title("LPG Price Trend (Jan–Mar 2026)")
    plt.grid()

    file1 = os.path.join(output_folder, "lpg_price_trend.png")
    plt.savefig(file1)
    plt.close()

    # -----------------------------
    # 4. LPG vs PG RENT
    # -----------------------------
    plt.figure()
    df.groupby('Date')[['LPG_Price','PG_Rent']].mean().plot(marker='o')
    plt.title("LPG Price vs PG Rent")
    plt.grid()

    file2 = os.path.join(output_folder, "lpg_vs_rent.png")
    plt.savefig(file2)
    plt.close()

    # -----------------------------
    # 5. HOUSEHOLD EXPENSE
    # -----------------------------
    plt.figure()
    df.groupby('Date')['Household_Expense'].mean().plot(marker='o')
    plt.title("Household Expense Trend")
    plt.grid()

    file3 = os.path.join(output_folder, "household_expense.png")
    plt.savefig(file3)
    plt.close()

    # -----------------------------
    # 6. CITY ANALYSIS
    # -----------------------------
    plt.figure()
    df.groupby('City')['Household_Expense'].mean().plot(kind='bar')
    plt.title("City-wise Expense")
    plt.grid()

    file4 = os.path.join(output_folder, "city_expense.png")
    plt.savefig(file4)
    plt.close()

    # -----------------------------
    # PRINT OUTPUT LOCATION
    # -----------------------------
    print("\n✅ Graphs saved here:")
    print(os.path.abspath(output_folder))

# -----------------------------
# RUN
# -----------------------------
if __name__ == "__main__":
    main()