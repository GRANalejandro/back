import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()

DB_NAME = "sqlite:///./test.db"  # Cambia la conexión a SQLite local
engine = create_engine(DB_NAME)

localSession = sessionmaker(autoflush=False, autocommit=False, bind=engine)

Base = declarative_base()