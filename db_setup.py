
from config import engine, SessionLocal, Base
from models import User, Category, Expense

def init_db():
    Base.metadata.create_all(bind=engine)

if __name__ == '__main__':
    init_db()