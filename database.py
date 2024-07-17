from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database URL
db_url = "postgresql://postgres:postgresql@localhost:5432/Person"
# Creates SQLAlchemy Engine
engine = create_engine(db_url, echo=True)

# Base class for models
Base = declarative_base()

# Create a configured session class
# autocommit=False: Transactions are not automatically committed.
# autoflush=False: Changes are not automatically flushed to the database.
# bind=engine: Connect this session factory to the specified database engine.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)