from Finance_tracker.transaction_add import add_transaction
from transaction_search import search_by_feature, search_by_date_range, search_by_amount, search_by_category,   search_by_type
from Finance_tracker.transaction_view import view_transactions  # Assuming this is defined in transaction_view.py
from transaction_edit import edit_transaction  # Assuming this is defined in transaction_edit.py
from transaction_group import group_by_category  # Assuming this is defined in transaction_group.py
from Finance_tracker.transaction_delete import delete_transaction  # Assuming this is defined in transaction_delete.py
from Finance_tracker.transaction_export import export_to_csv  # Assuming this is defined in transaction_export.py


def main_menu():
    while True:
        print("\n--- Personal Finance Tracker ---")
        print("1. Add Transaction")
        print("2. View Transactions by Date")
        print("3. Search Transaction by Feature")
        print("4. Edit Transaction by ID")
        print("5. Group Transactions by Category")
        print("6. Delete Transaction")
        print("7. Export to CSV")
        print("8. Search Transactions by Date Range")
        print("9. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_transaction()
        elif choice == '2':
            view_transactions()  # Ensuring the view logic is handled here
        elif choice == '3':
            # Menu for searching by feature
            print("\nSearch Transaction by Feature")
            print("1. By Date")
            print("2. By Amount")
            print("3. By Category")
            print("4. By Type")
            search_choice = input("Enter your choice (1-4): ").strip()

            if search_choice == '1':
                search_by_feature()  # Search by Date
            elif search_choice == '2':
                search_by_amount()  # Search by Amount
            elif search_choice == '3':
                search_by_category()  # Search by Category
            elif search_choice == '4':
                search_by_type()  # Search by Type
            else:
                print("Invalid choice. Please try again.")

        elif choice == '4':
            edit_transaction()  # Edit transaction logic here
        elif choice == '5':
            group_by_category()  # Group transactions by category
        elif choice == '6':
            delete_transaction()  # Delete transaction by ID
        elif choice == '7':
            export_to_csv()  # Export transactions to CSV
        elif choice == '8':
            search_by_date_range()  # Search by date range
        elif choice == '9':
            break
        else:
            print("Invalid choice. Please try again.")
main_menu()
