from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

import crud
from database import engine, localSession
from schemas import UserData, UserId, MoviesData, MoviesId
from models import Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",  # Agrega el puerto que estés usando para el frontend
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

def get_db():
    db = localSession()
    try: 
        yield db
    finally:
        db.close()

@app.get('/')
def root():
    return 'Hi, my Name is FastApi'

@app.get('/api/users/', response_model=list[UserId])
def get_users(db: Session = Depends(get_db)):
    return crud.get_users(db=db)

@app.get('/api/movies/', response_model=list[MoviesId])
def get_movies(db: Session = Depends(get_db)):
    return crud.get_movies(db=db)





@app.get('/api/users/{id:int}', response_model=UserId)
def get_user(id, db: Session = Depends(get_db)):
    user_by_id = crud.get_user_by_id(db=db, id=id)
    if user_by_id:
        return user_by_id
    raise HTTPException(status_code=404, detail='User not Found!!!')

@app.get('/api/movies/{id:int}', response_model=MoviesId)
def get_movies(id, db: Session = Depends(get_db)):
    Movies_by_id = crud.get_movies_by_id(db=db, id=id)
    if Movies_by_id:
        return Movies_by_id
    raise HTTPException(status_code=404, detail='User not Found!!!')



@app.post('/api/users/', response_model=UserId)
def create_user(user: UserData, db: Session = Depends(get_db)):
    check_name = crud.get_user_by_name(db=db, name=user.name)
    if check_name:
        raise HTTPException(status_code=400, detail='User already exist.')
    return crud.create_user(db=db, user=user)

@app.post('/api/movies/', response_model=MoviesId)
def create_movies(movie: MoviesData, db: Session = Depends(get_db)):
    return crud.create_movies(db=db, movie=movie)

