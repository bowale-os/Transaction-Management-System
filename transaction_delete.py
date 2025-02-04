from data import get_db_connection

def delete_transaction():
    print("\nWhat attribute would you like to delete by?")
    print("1. Date")
    print("2. Amount")
    print("3. Category")
    print("4. Type")
    choice = input("Enter your choice (1-4): ").strip()

    # Establish connection with the database
    conn = get_db_connection()
    cursor = conn.cursor()

    if choice == "1":  # Delete by Date
        date = input("Enter the date (YYYY-MM-DD): ")
        cursor.execute("DELETE FROM transactions WHERE date = ?", (date,))
    elif choice == "2":  # Delete by Amount
        try:
            amount = float(input("Enter the amount: "))
            cursor.execute("DELETE FROM transactions WHERE amount = ?", (amount,))
        except ValueError:
            print("Invalid input. Please enter a valid amount.")
            conn.close()
            return
    elif choice == "3":  # Delete by Category
        category = input("Enter the category: ")
        cursor.execute("DELETE FROM transactions WHERE category = ?", (category,))
    elif choice == "4":  # Delete by Type
        transaction_type = input("Enter the type (income/expense): ")
        cursor.execute("DELETE FROM transactions WHERE type = ?", (transaction_type,))
    else:
        print("Invalid choice.")
        conn.close()
        return

    # Commit the changes to the database
    conn.commit()

    # Check if any rows were deleted
    if cursor.rowcount > 0:
        print("Transaction(s) deleted successfully.")
    else:
        print("No matching transactions found to delete.")

    # Close the database connection
    conn.close()
