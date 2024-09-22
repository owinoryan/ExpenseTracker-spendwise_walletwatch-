from sqlalchemy.orm import Session
from db_setup import SessionLocal, init_db
from models.user import User
from models.category import Category
from models.expense import Expense

# Initialize the database
init_db()

def add_user():
    """Add a new user"""
    name = input("Enter user name: ")
    email = input("Enter user email: ")
    session = SessionLocal()
    user = User(name=name, email=email)
    session.add(user)
    session.commit()
    print(f"User {name} added!")

def add_category():
    """Add a new category"""
    name = input("Enter category name: ")
    session = SessionLocal()
    category = Category(name=name)
    session.add(category)
    session.commit()
    print(f"Category {name} added!")

def add_expense():
    """Add a new expense"""
    amount = float(input("Enter expense amount: "))
    description = input("Enter description: ")
    user_id = int(input("Enter user ID: "))
    category_id = int(input("Enter category ID: "))
    session = SessionLocal()
    expense = Expense(amount=amount, description=description, user_id=user_id, category_id=category_id)
    session.add(expense)
    session.commit()
    print(f"Expense added: {description}, Amount: {amount}")

def view_expenses():
    """View all expenses"""
    session = SessionLocal()
    expenses = session.query(Expense).all()
    if not expenses:
        print("No expenses found.")
    else:
        for exp in expenses:
            # Check if category or user is None and provide a fallback
            category_name = exp.category.name if exp.category else "No Category"
            user_name = exp.user.name if exp.user else "No User"
            print(f"{exp.id} - {exp.description}, {exp.amount}, Category: {category_name}, User: {user_name}")


def delete_expense():
    """Delete an expense"""
    expense_id = int(input("Enter expense ID to delete: "))
    session = SessionLocal()
    expense = session.query(Expense).get(expense_id)
    if expense:
        session.delete(expense)
        session.commit()
        print(f"Deleted expense {expense_id}")
    else:
        print(f"Expense with ID {expense_id} not found.")

def show_menu():
    """Display the menu and handle user selection"""
    while True:
        print("\nSpendwise Walletwatch Expense Tracker")
        print("1. Add User")
        print("2. Add Category")
        print("3. Add Expense")
        print("4. View Expenses")
        print("5. Delete Expense")
        print("6. Quit")

        # Get user's choice
        choice = input("Select an option (1-6): ")

        # Handle the user's choice
        if choice == '1':
            add_user()
        elif choice == '2':
            add_category()
        elif choice == '3':
            add_expense()
        elif choice == '4':
            view_expenses()
        elif choice == '5':
            delete_expense()
        elif choice == '6':
            print("Exiting Spendwise Walletwatch. Goodbye!")
            break
        else:
            print("Invalid option. Please choose a valid number from 1 to 6.")

# Entry point for the program
if __name__ == '__main__':
    show_menu()
