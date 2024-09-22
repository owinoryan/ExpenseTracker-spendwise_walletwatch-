from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Database connection URL (change to your appropriate path)
DATABASE_URL = "sqlite:///spendwise_walletwatch.db"

# Set up engine
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a Base class for model definitions
Base = declarative_base()
