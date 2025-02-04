# **Transaction Management System**  

An **SQLite and Python-based local transaction management system** designed to track **spending and income** efficiently. This CLI-based tool allows users to **add, edit, and manage financial transactions** while ensuring data integrity and usability.  

## **Features**  
✅ **Add Transactions** – Input date, amount, category, and type (income/expense).  
✅ **Edit Transactions** – Modify transaction details with a built-in **'same' feature** to retain existing values.  
✅ **Data Validation** – Ensures correct date formats, prevents invalid numerical entries, and maintains consistency.  
✅ **SQLite Integration** – Uses a lightweight **SQL database** for efficient storage and retrieval.  
✅ **Error Handling** – Detects invalid inputs and prevents data corruption.  
✅ **Transaction Overview** – Retrieve and review all past transactions for better financial insights.  

## **Installation**  
### **Prerequisites**  
Ensure you have **Python 3.x** installed on your system. Install SQLite if not already available.  

### **Setup Instructions**  
1. **Clone the repository:**  
   ```bash
   git clone https://github.com/yourusername/Transaction-Management-System.git
   cd Transaction-Management-System
   ```  
2. **Install dependencies:**  
   ```bash
   pip install -r requirements.txt
   ```  
3. **Run the application:**  
   ```bash
   python transaction_add.py
   ```  

## **Usage**  
- **Adding a transaction:**  
  ```bash
  Enter date (YYYY-MM-DD): 2025-01-15  
  Enter amount: 100  
  Enter category: Groceries  
  Type (income/expense): expense  
  ```
  _Output: Transaction added successfully!_  

- **Editing a transaction:**  
  ```bash
  Enter the transaction ID you want to edit: 5  
  Enter new date (current: 2025-01-15 or 'same' to keep): same  
  Enter new amount (current: 100): 120  
  Enter new category (current: Groceries): Food  
  Enter new type (current: expense): same  
  ```
  _Output: Transaction ID 5 has been updated successfully!_  

## **Database Schema (SQLite)**  
```sql
CREATE TABLE transactions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT NOT NULL,
    amount REAL NOT NULL,
    category TEXT NOT NULL,
    type TEXT CHECK(type IN ('income', 'expense')) NOT NULL
);
```  

## **Future Improvements**  
🔹 Add a **Graphical User Interface (GUI)** using **Tkinter or Flask**  
🔹 Implement **data visualization** with **Matplotlib/Seaborn**  
🔹 Enable **exporting transactions to CSV/Excel** for better financial tracking  

## **Contributing**  
Feel free to contribute by submitting **pull requests** or reporting issues.  

## **License**  
This project is open-source and available under the **MIT License**.  
