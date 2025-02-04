from data import get_db_connection
from datetime import datetime

# Function to search transactions by feature (Date, Amount, Category, Type)
def search_by_feature():
    print("\nWhat feature would you like to search by?")
    print("1. Date")
    print("2. Amount")
    print("3. Category")
    print("4. Type")
    choice = input("Enter your choice (1-4): ").strip()

    conn = get_db_connection()
    cursor = conn.cursor()

    if choice == "1":  # Search by Date
        search_date = input("Enter the date (YYYY-MM-DD): ")
        try:
            datetime.strptime(search_date, "%Y-%m-%d")  # Validate date format
            cursor.execute("SELECT id, date, amount, category, type FROM transactions WHERE date = ?", (search_date,))
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")
            conn.close()
            return

    elif choice == "2":  # Search by Amount
        try:
            amount = float(input("Enter the amount: "))
            cursor.execute("SELECT id, date, amount, category, type FROM transactions WHERE amount = ?", (amount,))
        except ValueError:
            print("Invalid amount format. Please enter a valid amount.")
            conn.close()
            return

    elif choice == "3":  # Search by Category
        category = input("Enter the category: ").capitalize()
        cursor.execute("SELECT id, date, amount, category, type FROM transactions WHERE category = ?", (category,))

    elif choice == "4":  # Search by Type
        transaction_type = input("Enter the type (income/expense): ")
        cursor.execute("SELECT id, date, amount, category, type FROM transactions WHERE type = ?", (transaction_type,))

    else:
        print("Invalid choice.")
        conn.close()
        return

    rows = cursor.fetchall()

    if rows:
        for row in rows:
            print(f"ID: {row[0]}, Date: {row[1]}, Amount: {row[2]}, Category: {row[3]}, Type: {row[4]}")
    else:
        print("No transactions found with the given criteria.")

    conn.close()

# Function to search transactions by date range
def search_by_date_range():
    start_date = input("Enter the start date (YYYY-MM-DD): ")
    end_date = input("Enter the end date (YYYY-MM-DD): ")

    try:
        datetime.strptime(start_date, "%Y-%m-%d")
        datetime.strptime(end_date, "%Y-%m-%d")

        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT id, date, amount, category, type FROM transactions WHERE date BETWEEN ? AND ?",
                       (start_date, end_date))
        rows = cursor.fetchall()

        if rows:
            print(f"\nTransactions between {start_date} and {end_date}:")
            for row in rows:
                print(f"ID: {row[0]}, Date: {row[1]}, Amount: {row[2]}, Category: {row[3]}, Type: {row[4]}")
        else:
            print("No transactions found in the given date range.")

        conn.close()
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")

# Additional search functions

# Search transactions by amount
def search_by_amount():
    try:
        amount = float(input("Enter the amount: "))
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, date, amount, category, type FROM transactions WHERE amount = ?", (amount,))
        rows = cursor.fetchall()

        if rows:
            for row in rows:
                print(f"ID: {row[0]}, Date: {row[1]}, Amount: {row[2]}, Category: {row[3]}, Type: {row[4]}")
        else:
            print("No transactions found with the given amount.")
        conn.close()
    except ValueError:
        print("Invalid amount format. Please enter a valid amount.")

# Search transactions by category
def search_by_category():
    category = input("Enter the category: ").capitalize()
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, date, amount, category, type FROM transactions WHERE category = ?", (category,))
    rows = cursor.fetchall()

    if rows:
        for row in rows:
            print(f"ID: {row[0]}, Date: {row[1]}, Amount: {row[2]}, Category: {row[3]}, Type: {row[4]}")
    else:
        print("No transactions found with the given category.")
    conn.close()

# Search transactions by type
def search_by_type():
    transaction_type = input("Enter the type (income/expense): ")
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, date, amount, category, type FROM transactions WHERE type = ?", (transaction_type,))
    rows = cursor.fetchall()

    if rows:
        for row in rows:
            print(f"ID: {row[0]}, Date: {row[1]}, Amount: {row[2]}, Category: {row[3]}, Type: {row[4]}")
    else:
        print("No transactions found with the given type.")
    conn.close()
