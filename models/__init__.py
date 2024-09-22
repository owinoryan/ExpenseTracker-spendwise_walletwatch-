
from .user import User
from .category import Category
from .expense import Expense

# Import the 'declarative_base' function from SQLAlchemy's ORM, 
# which is needed to create the base class for declarative model definitions
from sqlalchemy.ext.declarative import declarative_base

# Create an instance of the base class, which all ORM models will inherit from.
# This 'Base' class is the foundation for all the database tables that will be created.
Base = declarative_base()

