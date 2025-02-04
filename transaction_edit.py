from data import get_db_connection
import datetime

def edit_transaction():
    # Prompt for the transaction ID
    transaction_id = input("Enter the transaction ID you want to edit: ").strip()

    conn = get_db_connection()
    cursor = conn.cursor()

    # Check if the transaction exists
    cursor.execute("SELECT * FROM transactions WHERE id = ?", (transaction_id,))
    transaction = cursor.fetchone()

    if transaction:
        print(f"\nCurrent details of transaction ID {transaction_id}:")
        print(f"Date: {transaction[1]}")
        print(f"Amount: {transaction[2]}")
        print(f"Category: {transaction[3]}")
        print(f"Type: {transaction[4]}")

        # Ask user for new values with 'same' option
        new_date = input(f"Enter new date (current: {transaction[1]} or 'same' to keep): ").strip()
        if new_date.lower() == 'same' or not new_date:
            new_date = transaction[1]
        else:
            try:
                datetime.datetime.strptime(new_date, "%Y-%m-%d")  # Validate date format
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD.")
                conn.close()
                return

        new_amount = input(f"Enter new amount (current: {transaction[2]} or 'same' to keep): ").strip()
        if new_amount.lower() == 'same' or not new_amount:
            new_amount = transaction[2]
        elif not new_amount.replace('.', '', 1).isdigit():
            print("Invalid amount. Please enter a valid number.")
            conn.close()
            return

        new_category = input(f"Enter new category (current: {transaction[3]} or 'same' to keep): ").strip()
        if new_category.lower() == 'same' or not new_category:
            new_category = transaction[3]

        new_type = input(f"Enter new type (current: {transaction[4]} or 'same' to keep): ").strip()
        if new_type.lower() == 'same' or not new_type:
            new_type = transaction[4]

        # Update the transaction
        cursor.execute(
            "UPDATE transactions SET date = ?, amount = ?, category = ?, type = ? WHERE id = ?",
            (new_date, new_amount, new_category, new_type, transaction_id)
        )

        # Commit the changes and inform the user
        conn.commit()
        print(f"\nTransaction ID {transaction_id} has been updated successfully.")
    else:
        print(f"\nTransaction with ID {transaction_id} not found.")

    conn.close()
