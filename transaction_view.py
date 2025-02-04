from data import get_db_connection

# Function to view transactions from the database by date
def view_transactions():
    search_date = input("Enter the date (YYYY-MM-DD): ")

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT id, date, amount, category, type FROM transactions WHERE date = ?", (search_date,))
    rows = cursor.fetchall()

    if rows:
        print("\nTransactions on", search_date)
        for row in rows:
            print(f"ID: {row[0]}, Date: {row[1]}, Amount: {row[2]}, Category: {row[3]}, Type: {row[4]}")
    else:
        print("No transactions found for the given date.")

    conn.close()

# Function to view all transactions (just as an example, you might want to add more logic)
def view_all_transactions():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT id, date, amount, category, type FROM transactions")
    rows = cursor.fetchall()

    if rows:
        print("\n--- All Transactions ---")
        for row in rows:
            print(f"ID: {row[0]}, Date: {row[1]}, Amount: {row[2]}, Category: {row[3]}, Type: {row[4]}")
    else:
        print("No transactions found.")

    conn.close()

# Additional functions can be added based on your requirements (e.g., view by category)
