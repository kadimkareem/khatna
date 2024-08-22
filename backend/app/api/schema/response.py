
from sqlmodel import SQLModel


class Response(SQLModel):
    data:any
    message:str
    status_code:int