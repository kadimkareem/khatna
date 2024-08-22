from fastapi import HTTPException
from sqlmodel import SQLModel 



class Error(SQLModel,HTTPException):
    msg: str
    code:int




