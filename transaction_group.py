from data import get_db_connection

def group_by_category():
    # Connect to the database
    conn = get_db_connection()
    cursor = conn.cursor()

    # Query to group transactions by category and calculate the sum of amounts
    cursor.execute("SELECT category, SUM(amount) FROM transactions GROUP BY category")
    rows = cursor.fetchall()

    # Check if there are any results and display them
    if rows:
        print("\n--- Transactions Grouped by Category ---")
        for row in rows:
            print(f"Category: {row[0]}, Total Amount: {row[1]}")
    else:
        print("No transactions found.")

    # Close the database connection
    conn.close()
