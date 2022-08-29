from lib2to3.pytree import Base
from xmlrpc.client import boolean
from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

from pydantic.types import conint

# class Post(BaseModel):
#     title: str 
#     content: str 
#     published: bool = True

# ------User Class----------------
class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserResp(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        orm_mode = True

# ----- End of User Class ----------

# ------Post Class----------------
class PostBase(BaseModel):
    title: str 
    content: str 
    published: bool = True

class PostCreate(PostBase):
    pass

class Post(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: UserResp

    class Config:
        orm_mode = True

class PostOut(BaseModel):
    Post: Post
    votes: int

    class Config:
        orm_mode = True


# ----- End of Post Class ----------
 


# ------UserLogin Class----------------
class UserLogin(BaseModel):
    email: EmailStr
    password: str

#-----Login Authentication class---------------
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[str] = None


#--------------Class Vote---------------------
class Vote(BaseModel):
    post_id: int
    dir: conint(le=1)
