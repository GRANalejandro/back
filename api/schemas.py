from pydantic import BaseModel
from typing import Union

class UserData(BaseModel):
    name: str
    password: str

class UserId(UserData):
    id: int

class MoviesData(BaseModel):
    movieImageUrl: Union[str, int]
    MovieUrl: Union[str, int]

class MoviesId(MoviesData):
    id: int