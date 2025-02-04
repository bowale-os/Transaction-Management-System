from data import get_db_connection
import sqlite3
from datetime import datetime

def add_transaction():
    while True:
        date = input("Enter date (YYYY-MM-DD): ").strip()
        try:
            date_obj = datetime.strptime(date, "%Y-%m-%d")  # Validate date format
            if date_obj.year < 2025:
                raise ValueError("Date must be in 2025 or later.")
            break
        except ValueError as e:
            print(f"Invalid date: {e}")

    while True:
        amount = input("Enter amount: ").strip()
        try:
            amount = float(amount)
            if amount <= 0:
                raise ValueError("Amount must be greater than zero.")
            break
        except ValueError:
            print("Invalid amount. Please enter a positive numeric value.")

    while True:
        category = input("Enter category: ").strip()
        if category:
            break
        print("Category cannot be empty. Please enter a valid category.")

    while True:
        transaction_type = input("Type (income/expense): ").strip().lower()
        if transaction_type in ["income", "expense"]:
            break
        print("Invalid type. Please enter 'income' or 'expense'.")

    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("INSERT INTO transactions (date, amount, category, type) VALUES (?, ?, ?, ?)",
                       (date, amount, category, transaction_type))

        conn.commit()
        print("Transaction added successfully!")

    except sqlite3.Error as e:
        print(f"Database error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    finally:
        conn.close()
