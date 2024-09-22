
from sqlalchemy import Column, Integer, String

from config import Base

# Define a Category class, which will represent a table in the database
class Category(Base):
    # Set the table name for this model to 'categories'
    __tablename__ = 'categories'

    # Define the columns of the table:
    # id column, of type Integer, acts as the primary key for each record and will be indexed for fast lookups
    id = Column(Integer, primary_key=True, index=True)

    # name column, of type String, cannot be null (nullable=False), meaning it is a required field
    name = Column(String, nullable=False)

    # Define a method for how instances of this class should be represented 
    def __repr__(self):
        # Return a string representation that shows the category name when the object is printed or logged
        return f"<Category(name={self.name})>"
