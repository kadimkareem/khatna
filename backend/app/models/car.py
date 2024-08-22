
# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring



from datetime import datetime
from enum import Enum
from app.models.trip import Trip
from typing import Optional
from sqlmodel import Field, Relationship ,SQLModel ,MetaData,Column,func,DateTime



class CarType(str, Enum):
    bus = "minibus"
    van = "van"
    sedan = "sedan"

class BaseCar(SQLModel):
    model : Optional[str] =None
    license_plate : Optional[str] =None
    year:Optional[int] =None
    color : Optional[str] =None
    photo: Optional[str] =None
    capacity :Optional[int]  =None
    type:Optional[CarType] =None
    driver_id:int

class Car(BaseCar, table=True):

    id: int | None = Field(default=None, primary_key=True)
    created_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), server_default=func.now()))
    updated_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now()))
    
    license_plate:str = Field(unique=True,nullable=True)

    driver_id: int |None = Field( default=None,foreign_key="driver.id", nullable=False,) # uniq=False cuz driver will have more than one car
    driver: "Driver" = Relationship(back_populates="car", sa_relationship_kwargs={'uselist': False},)

    trips:"Trip" = Relationship(back_populates="car")




#--------schemas----------

class CreateCar(SQLModel):
    license_plate : Optional[str]
    model : Optional[str]
    year:Optional[int] 
    color : Optional[str]
    photo: Optional[str]
    capacity :int
    type:CarType
    # driver_id: int get it from request and put it in the Car model directly by car.driver_id=activeusr.id
    #then we user car=Car.model_validate(car_in)
#
class UpdateCar(SQLModel):
    model : Optional[str] =None
    license_plate : Optional[str] =None
    year:Optional[int] =None
    color : Optional[str] =None
    photo: Optional[str] =None
    capacity :Optional[int]  =None
    type:Optional[CarType] =None


class CarOut(BaseCar):
    id: int


class CarsOut(BaseCar):
    data: list[CarOut]
    count: int

