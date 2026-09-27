# Expense Tracker & Analyzer

## Project Overview

Expense Tracker & Analyzer is a Python-based command-line application that helps users record, manage, and analyze their daily expenses.

The application allows users to add, view, search, update, and delete expenses. It also provides useful analysis such as total spending, average expense, highest and lowest expenses, category-wise spending, and monthly spending.

The project uses a CSV file to store expense data so that the information remains available even after the program is closed.

---

## Objectives

The main objectives of this project are:

- To provide a simple way to record daily expenses.
- To allow users to manage their expense records.
- To analyze spending patterns.
- To organize expenses based on categories and dates.
- To practice Python programming concepts such as functions, classes, file handling, validation, lists, dictionaries, and exception handling.

---

## Features

### 1. Add Expense
Users can add a new expense by entering:

- Description
- Amount
- Category
- Date

Each expense is automatically assigned a unique ID.

### 2. View All Expenses
Displays all saved expenses in a structured table.

### 3. Search Expense
Users can search for expenses using:

- Description
- Category

### 4. Update Expense
Users can update an existing expense using its expense ID.

### 5. Delete Expense
Users can delete an expense after confirming the deletion.

### 6. Expense Analysis
The application calculates:

- Total spending
- Average expense
- Highest expense
- Lowest expense
- Category-wise spending
- Highest spending category

### 7. Generate Report
A summary report is generated containing:

- Number of expenses
- Total spending
- Average expense
- Highest expense
- Lowest expense
- Category-wise spending
- Monthly spending

### 8. Data Validation
The application checks:

- Amount is a valid positive number.
- Description is not empty.
- Category is not empty.
- Date follows the DD-MM-YYYY format.

---

## Technologies Used

- Python 3
- CSV File Handling
- Object-Oriented Programming
- Python Functions
- Lists and Dictionaries
- Exception Handling
- Unit Testing

No external Python libraries are required.

---

## Project Structure

```text
expense-tracker/
│
├── data/
│   └── expenses.csv
│
├── tests/
│   └── test_analyzer.py
│
├── analyzer.py
├── expense.py
├── expense_manager.py
├── file_handler.py
├── main.py
├── report.py
├── validator.py
│
├── README.md
├── requirements.txt
└── statement.md
