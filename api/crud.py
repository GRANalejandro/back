from sqlalchemy.orm import Session

from models import User, Movies
from schemas import UserData, MoviesData

def get_users(db: Session): 
    return db.query(User).all()

def get_user_by_id(db: Session, id: int):
    return db.query(User).filter(User.id == id).first()

def get_user_by_name(db: Session, name: str):
    return db.query(User).filter(User.name == name).first()

def create_user(db: Session, user: UserData):
    fake_password = user.password + '#fake' 
    new_user = User(name=user.name, password=fake_password)
    db.add(new_user)
    db.commit()
    db.flush(new_user)
    return new_user

def get_movies(db: Session): 
    return db.query(Movies).all()

def get_movies_by_id(db: Session, id: int):
    return db.query(Movies).filter(Movies.id == id).first()

def create_movies(db: Session, movie: MoviesData):
    new_movie = Movies(movieImageUrl=movie.movieImageUrl, MovieUrl=movie.MovieUrl)
    db.add(new_movie)
    db.commit()
    db.flush(new_movie)
    return new_movie