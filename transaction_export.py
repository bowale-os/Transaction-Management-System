import csv
from data import get_db_connection

def export_to_csv():
    # Connect to the database
    conn = get_db_connection()
    cursor = conn.cursor()

    # Fetch all transactions from the database
    cursor.execute("SELECT id, date, amount, category, type FROM transactions")
    rows = cursor.fetchall()

    # If no rows are found, print a message and return
    if not rows:
        print("No transactions found to export.")
        conn.close()
        return

    # Ask for the filename to export
    filename = input("Enter the filename to export transactions to (e.g., transactions.csv): ")

    # Write the transactions to the CSV file
    try:
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)

            # Write the header
            writer.writerow(["ID", "Date", "Amount", "Category", "Type"])

            # Write the transaction data
            for row in rows:
                writer.writerow(row)

        print(f"Transactions successfully exported to {filename}.")
    except Exception as e:
        print(f"An error occurred while exporting to CSV: {e}")

    # Close the database connection
    conn.close()
