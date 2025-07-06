import csv
from datetime import datetime
import matplotlib.pyplot as plt
from collections import defaultdict

DATA_FILE = "expenses.csv"

def load_data():
    try:
        with open(DATA_FILE, mode='r', newline='') as f:
            reader = csv.DictReader(f)
            return list(reader)
    except FileNotFoundError:
        return []

def save_expense(date, category, amount):
    try:
        with open(DATA_FILE, mode='r') as f:
            file_exists = True
    except FileNotFoundError:
        file_exists = False

    with open(DATA_FILE, mode='a', newline='') as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(['date', 'category', 'amount'])
        writer.writerow([date, category, amount])

def add_expense():
    try:
        date_input = input("Enter date (DD-MM-YYYY): ")
        date = datetime.strptime(date_input, "%d-%m-%Y").strftime("%Y-%m-%d")
    except ValueError:
        print("❗ Invalid date format. Please use DD-MM-YYYY.")
        return

    category = input("Enter category (e.g. food, transport): ").strip().lower()
    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("❗ Invalid amount.")
        return

    save_expense(date, category, amount)
    print("✅ Expense added.")

def show_monthly_totals():
    try:
        month_input = input("Enter month to view totals (MM-YYYY): ")
        month = datetime.strptime("01-" + month_input, "%d-%m-%Y").strftime("%Y-%m")
    except ValueError:
        print("❗ Invalid month format. Please use MM-YYYY.")
        return

    data = load_data()
    totals = defaultdict(float)

    for row in data:
        if row['date'].startswith(month):
            totals[row['category']] += float(row['amount'])

    if not totals:
        print(f"❗ No data for {month_input}.")
        return

    print(f"\nMonthly totals for {month_input}:")
    for cat, amt in totals.items():
        print(f"  {cat}: ₹{amt:.2f}")

def plot_chart():
    try:
        month_input = input("Enter month for visualization (MM-YYYY): ")
        month = datetime.strptime("01-" + month_input, "%d-%m-%Y").strftime("%Y-%m")
    except ValueError:
        print("❗ Invalid month format. Please use MM-YYYY.")
        return

    chart_type = input("Choose chart type (pie/bar): ").strip().lower()
    data = load_data()
    totals = defaultdict(float)

    for row in data:
        if row['date'].startswith(month):
            totals[row['category']] += float(row['amount'])

    categories = list(totals.keys())
    amounts = list(totals.values())

    if not categories:
        print("❗ No data for the selected month.")
        return

    if chart_type == 'pie':
        plt.pie(amounts, labels=categories, autopct='%1.1f%%')
        plt.title(f"Expense Distribution - {month_input}")
    elif chart_type == 'bar':
        plt.bar(categories, amounts)
        plt.title(f"Expense Distribution - {month_input}")
        plt.ylabel("Amount (₹)")
    else:
        print("❗ Invalid chart type.")
        return

    plt.tight_layout()
    plt.show()

def menu():
    while True:
        print("\n--- Expense Tracker CLI (CSV, No os) ---")
        print("1. Add Expense")
        print("2. Show Monthly Totals")
        print("3. Plot Chart")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            show_monthly_totals()
        elif choice == '3':
            plot_chart()
        elif choice == '4':
            print("👋 Exiting. Goodbye!")
            break
        else:
            print("❗ Invalid option. Try again.")

if __name__ == "__main__":
    menu()