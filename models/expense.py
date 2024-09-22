
from sqlalchemy import Column, Integer, String, ForeignKey, Float
# Import relationship function to define relationships between tables
from sqlalchemy.orm import relationship
# Import Base class from config, used for creating models
from config import Base

# Define an Expense class, which represents the 'expenses' table in the database
class Expense(Base):
    # Set the table name for this model to 'expenses'
    __tablename__ = 'expenses'

    # Define the columns of the table:
    # id column: Integer type, acts as the primary key and is indexed for fast lookups
    id = Column(Integer, primary_key=True, index=True)

    # amount column: Float type, stores the expense amount, and cannot be null (nullable=False)
    amount = Column(Float, nullable=False)

    # description column: String type, stores a description of the expense, and cannot be null (nullable=False)
    description = Column(String, nullable=False)

    # category_id column: Integer type, references the id field in the 'categories' table
    # ForeignKey enforces the relationship between 'expenses' and 'categories'
    category_id = Column(Integer, ForeignKey('categories.id'))

    # user_id column: Integer type, references the id field in the 'users' table
    # ForeignKey enforces the relationship between 'expenses' and 'users'
    user_id = Column(Integer, ForeignKey('users.id'))

    # Define the relationship between Expense and Category using the category_id ForeignKey
    # This creates a connection to the Category table and allows for accessing the related category object
    category = relationship("Category")

    # Define the relationship between Expense and User using the user_id ForeignKey
    # This creates a connection to the User table and allows for accessing the related user object
    user = relationship("User")

    # Define a method for how instances of this class should be represented as strings
    def __repr__(self):
        # Return a string representation that shows the expense amount and description
        # This is useful for debugging and logging
        return f"<Expense(amount={self.amount}, description={self.description})>"

