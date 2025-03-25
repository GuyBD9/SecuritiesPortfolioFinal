# SecuritiesPortfolioDEMO/views/portfolio_view.py
import matplotlib.pyplot as plt
import pandas as pd
from tabulate import tabulate
from database.db_manager import DatabaseManager

def get_portfolio_data():
    db = DatabaseManager()
    columns = ["Symbol", "Name", "Price", "Sector", "Volatility", "Type", "Stock Type", "Bond Type"]
    securities = db.get_all_securities() # tamplet list
    df = pd.DataFrame(securities, columns=columns)
    if len(df) > 0:
        share_allocation = round(100.0 / len(df), 2)
        df["Share (%)"] = share_allocation
    else:
        df["Share (%)"] = []
    return df

def display_table():
    df = get_portfolio_data()
    print("\nPortfolio Table:\n")
    table_data = df[["Name", "Symbol", "Price", "Share (%)"]]
    print(tabulate(table_data, headers="keys", tablefmt="grid"))

def plot_portfolio():
    df = get_portfolio_data()
    if df.empty:
        print("No data to display.")
        return
    plt.figure(figsize=(10, 6))
    plt.bar(df["Name"], df["Share (%)"])
    plt.xlabel("Security Name")
    plt.ylabel("Portfolio Share (%)")
    plt.title("Portfolio Composition")
    plt.xticks(rotation=45, ha="right")
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.tight_layout()
    plt.show()

def main():
    display_table()
    plot_portfolio()

if __name__ == "__main__":
    main()
