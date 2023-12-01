from sqlalchemy import Column, String, Integer

from database import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(30), index=True, unique=True)
    password = Column(String(30), index=True)

class Movies(Base):
    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True, index=True)
    movieImageUrl = Column(String(60), index=True)
    MovieUrl = Column(String(60), index=True)

