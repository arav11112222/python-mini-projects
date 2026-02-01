# Expense Tracker - Beginner Python Project

expenses = []

def add_expense():
    amount = float(input("Enter expense amount: "))
    category = input("Enter expense category: ")
    expenses.append((amount, category))
    print("Expense added successfully!")

def view_expenses():
    if len(expenses) == 0:
        print("No expenses recorded.")
        return

    print("\nRecorded Expenses:")
    for amount, category in expenses:
        print("Category:", category, "Amount:", amount)

def calculate_total():
    total = 0
    for amount, _ in expenses:
        total += amount
    print("Total Expense:", total)

while True:
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expense")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        calculate_total()
    elif choice == "4":
        print("Program ended.")
        break
    else:
        print("Invalid choice. Try again.")
