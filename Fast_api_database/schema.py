from pydantic import BaseModel
from typing import Optional


class UpdateUsers(BaseModel):
    name : Optional[str] = None
    email : Optional[str] = None
    password : Optional[str] = None

class UserParent(BaseModel):
    name: str
    email: str

class Users(UserParent):
    password: str
