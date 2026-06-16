import csv
import json
import os
from datetime import datetime

# Global file paths for data persistence
DATA_FILE = "data.json"


def main():
    transactions = load_data()
    budgets = {}  # Optional expansion: load/save budgets similarly

    while True:
        print("\n=== SMART BUDGET PLANNER ===")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Transactions")
        print("4. View Financial Summary")
        print("5. Export Data to CSV")
        print("6. Exit")

        choice = input("\nChoose an option: ").strip()

        if choice in ["1", "2"]:
            t_type = "income" if choice == "1" else "expense"
            try:
                amount = float(input("Enter amount: $"))
                if amount <= 0:
                    print("Amount must be greater than zero.")
                    continue
            except ValueError:
                print("Invalid input. Please enter a valid number.")
                continue

            category = input("Enter category (e.g., Salary, Food, Utilities): ").strip().capitalize()
            # Default to today's date if left blank
            date_input = input("Enter date (YYYY-MM-DD) or press Enter for today: ").strip()
            if not date_input:
                date_str = datetime.today().strftime("%Y-%m-%d")
            else:
                try:
                    datetime.strptime(date_input, "%Y-%m-%d")
                    date_str = date_input
                except ValueError:
                    print("Invalid date format. Using today's date.")
                    date_str = datetime.today().strftime("%Y-%m-%d")

            transactions = add_transaction(transactions, t_type, amount, category, date_str)
            save_data(transactions)
            print(f"Successfully added {t_type}!")

        elif choice == "3":
            if not transactions:
                print("No transactions recorded yet.")
                continue
            print(f"\n{'Date':<12} {'Type':<10} {'Category':<15} {'Amount':<10}")
            print("-" * 50)
            for t in transactions:
                print(f"{t['date']:<12} {t['type'].capitalize():<10} {t['category']:<15} ${t['amount']:<10.2f}")

        elif choice == "4":
            balance, total_inc, total_exp = calculate_balance(transactions)
            print("\n=== FINANCIAL SUMMARY ===")
            print(f"Total Income:   ${total_inc:.2f}")
            print(f"Total Expenses: ${total_exp:.2f}")
            print(f"Current Balance: ${balance:.2f}")

        elif choice == "5":
            filename = input("Enter export filename (e.g., report.csv): ").strip()
            if not filename.endswith(".csv"):
                filename += ".csv"
            if export_csv(transactions, filename):
                print(f"Data successfully exported to {filename}!")
            else:
                print("Failed to export data. No transactions found.")

        elif choice == "6":
            print("Thank you for using Smart Budget Planner. Goodbye!")
            break
        else:
            print("Invalid choice. Please select an option from 1 to 6.")


# --- CS50P REQUIRED CUSTOM FUNCTIONS ---

def add_transaction(transactions, transaction_type, amount, category, date_str):
    """Appends a new transaction dictionary to the transactions list."""
    new_transaction = {
        "type": transaction_type,
        "amount": float(amount),
        "category": category,
        "date": date_str
    }
    transactions.append(new_transaction)
    return transactions


def calculate_balance(transactions):
    """Calculates balance, total income, and total expenses. Returns a tuple."""
    total_income = sum(t["amount"] for t in transactions if t["type"] == "income")
    total_expense = sum(t["amount"] for t in transactions if t["type"] == "expense")
    balance = total_income - total_expense
    return balance, total_income, total_expense


def get_category_total(transactions, category):
    """Calculates total money associated with a specific category."""
    category = category.capitalize()
    return sum(t["amount"] for t in transactions if t["category"].capitalize() == category)


def export_csv(transactions, filename):
    """Exports data into a clean CSV format. Returns True if successful, False otherwise."""
    if not transactions:
        return False

    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Type", "Category", "Amount"])
        for t in transactions:
            writer.writerow([t["date"], t["type"], t["category"], t["amount"]])
    return True


# --- HELPER UTILITIES (File handling) ---

def load_data():
    """Loads transaction history from a JSON file."""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return []
    return []


def save_data(transactions):
    """Saves transaction history to a JSON file."""
    with open(DATA_FILE, "w") as file:
        # Pass both the data AND the file object ('file') to json.dump
        json.dump(transactions, file, indent=4)


if __name__ == "__main__":
    main()
