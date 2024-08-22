

from datetime import datetime
from app.models.driver import Driver
from app.models.passenger import Passenger
from typing import Optional
from sqlmodel import Field, Relationship, SQLModel ,Column,func,DateTime

__all__=(
    "UserBase",
    "UserCreate",
    "UserCreateOpen",
    "UserUpdate",
    "UserUpdateMe",
    "UpdatePassword",
    "User",
    "UserOut",
    "UsersOut",
    )
    
    
    
# Shared properties
# TODO replace email str with EmailStr when sqlmodel supports it
class UserBase(SQLModel):
    email: str = Field(unique=True, index=True)
    is_active: bool = True
    is_superuser: bool = False
    full_name: str | None = None
    # first_name: str | None = None
    # last_name: str | None = None
    # phone: str | None = Field(unique=True)



# Properties to receive via API on creation
class UserCreate(UserBase):
    password: str


# TODO replace email str with EmailStr when sqlmodel supports it
class UserCreateOpen(SQLModel):
    email: str
    password: str
    full_name: str | None = None


# Properties to receive via API on update, all are optional
# TODO replace email str with EmailStr when sqlmodel supports it
class UserUpdate(UserBase):
    email: str | None = None  # type: ignore
    password: str | None = None


# TODO replace email str with EmailStr when sqlmodel supports it
class UserUpdateMe(SQLModel):
    full_name: str | None = None
    email: str | None = None


class UpdatePassword(SQLModel):
    current_password: str
    new_password: str


# Database model, database table inferred from class name
class User(UserBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    hashed_password: str
    
    items: list["Item"] = Relationship(back_populates="owner")
    driver:Driver = Relationship(back_populates="user" ,sa_relationship_kwargs={'uselist': False},)
    passenger:"Passenger" = Relationship(back_populates="user", sa_relationship_kwargs={'uselist': False},)
    #attendances:list["Attendance"] = Relationship(back_populates="user")

    created_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), server_default=func.now()))
    updated_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now()))



# Properties to return via API, id is always required
class UserOut(UserBase):
    id: int


class UsersOut(SQLModel):
    data: list[UserOut]
    count: int

