from sqlalchemy import String, Integer, Column, Boolean
from database import Base, engine

# Function to create database tables
def create_tables():
    Base.metadata.create_all(engine)

# SQLAlchemy model for Person
class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True)
    first_name =  Column(String(40), nullable=False)
    last_name =  Column(String(40), nullable=False)
    is_Male =  Column(Boolean)

