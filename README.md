### Spendwise_Walletwatch

Spendwise_Walletwatch is a command-line interface (CLI) application designed to help users track their expenses, categorize them, and store them in a database. This project is built with Python using the SQLAlchemy ORM to manage database interactions and provides users with an easy way to keep track of their spending habits.

### Features

1. Add User: Create a new user to track expenses.
2. Add Category: Create a category to organize expenses.
3. Add Expense: Add an expense under a specific category and user.
4. View Expenses: View all recorded expenses, along with the category and user.
5. Delete Expense: Remove an expense by ID.
6. Quit: Exit the application
7. Database Management: The app uses a relational database to store all the data, with support for migrations using Alembic.

spendwise_walletwatch/
├── app.py # Main entry point for the CLI
├── models/
│ ├── **init**.py # Initializes SQLAlchemy models
│ ├── user.py # User model definition
│ ├── category.py # Category model definition
│ ├── expense.py # Expense model definition
├── migrations/ # Alembic migrations folder
│ └── env.py # Alembic environment
├── config.py # Database configuration
├── db_setup.py # Initialize database and ORM session
├── Pipfile # Pipenv environment file
├── README.md # Project documentation
└── spendwise_walletwatch.db # Project database

### Database Models

1. User Model (models/user.py)

# Fields:

id: Integer, primary key
name: String, name of the user
email: String, email address of the user

2. Category Model (models/category.py)

# Fields:

id: Integer, primary key
name: String, name of the category
description: String, optional description of the category

3. Expense Model (models/expense.py)

# Fields:

id: Integer, primary key
amount: Decimal, the amount spent
date: Date, date of the expense
description: String, optional description of the expense
user_id: Integer, foreign key referencing the users table
category_id: Integer, foreign key referencing the category table

## Relationships

Each Expense belongs to one User and one Category.
Each User can have multiple Expenses.
Each Category can have multiple Expenses.

### dbdiagram link

https://dbdiagram.io/d/spendwise_walletwatch-66eaf0afa0828f8aa6469b86

### CLI Features

The CLI provides an interactive way to manage users, categories, and expenses. Here's a list of the available commands:

### Menu Options:

1. Add User:
   Prompts for a user's name and email to create a new user.

2. Add Category:
   Prompts for a category name to organize expenses (e.g., Rent, Food).

3. Add Expense:
   Enter the amount, description, user ID, and category ID to add a new expense.

4. View Expenses:
   Displays all expenses along with the category and user associated with each expense.

5. Delete Expense:
   Enter the ID of the expense to be deleted.

6. Quit:
   Exit the application.

### Usage

After installing and setting up the project, run the application using:

python app.py

### Example

# Create a User:(1)

> Create User
> Enter Name: Ryan Giggs
> Enter Email: ryan.giggs@example.com
> User Ryan Giggs has been created.

### Create a Category: (2)

> Create Category
> Enter Category Name: Groceries
> Enter Description (Optional): Food and related items
> Category Groceries has been created.

### Add an Expense: (3)

> Add Expense
> Enter Amount: 500.00
> Enter Description (Optional): Weekly grocery shopping
> Enter User ID: 1
> Enter Category ID: 1
> Expense added successfully.

### View Expenses: (4)

> View Expenses
> User: Ryan Giggs

1. 500.00 KES for Groceries on 2024-09-18 (Weekly grocery shopping)

### Delete an Expense: (5)

> Delete Expense
> Enter Expense ID: 1
> Expense deleted successfully.

### Quit: (6)

> Exit the application.

### Database Schema

The project uses three tables: users, categories, and expenses, with the following relationships:

1. User: Represents a person who logs expenses.
2. Category: Represents an expense category (e.g., Groceries, Rent).
3. Expense: Represents an individual expense. Each expense is linked to a user and a category.
