

# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring


#the driver creates it's own car by making post on api/cars (not while creating driver profile)
#driver has only one car
#driver can create more  routes (maybe he works moret shifts )
#driver can create more trips


from typing import Optional
from app.models.car import Car
from datetime import datetime
from sqlmodel import Field, SQLModel, Relationship  ,Column,DateTime,func


# Database model, database table inferred from class name



class DriverBase(SQLModel):
    license_number:str|None =None
    license_expiry_date :datetime|None =None
    years_of_experience :int |None =None
    discription:str |None =None
    rating : float |None =None
    user_id:int |None 

class Driver(DriverBase, table=True):
    id:int|None = Field(default=None, primary_key=True, index=True)    

    user_id: int | None = Field(default=None, foreign_key="user.id",nullable=False, unique=True)

    user:"User" = Relationship(back_populates="driver")

    trips:list["Trip"] = Relationship( back_populates='driver') #driven_trips
    routes:list["Route"] = Relationship( back_populates='driver') #driven_trips
    car:Car = Relationship( back_populates="driver")

    created_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), server_default=func.now()))
    updated_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now()))




#--------schemas----------
class DriverCreate(SQLModel):
    license_number:str
    license_expiry_date :datetime
    years_of_experience :int 
    discription:str 
    #rating : float , | drive should not able to crate rating for him self , so the default raing will be 0 , and a separate end point will created for updateing rating for the driver by passengers
    #user_id:int get it from request and put it in the Driver model directly by driver.user_id=activeusr.id
    #then we user driver=Driver.model_validate(driver_in)
    # car:Car  |None =None  | no need creating by making update on api/cars/ with driver_id from auth , 
    
class DriverUpdate(SQLModel):
    license_number:str | None =None
    license_expiry_date:datetime | None =None
    years_of_experience :int   |None =None
    discription:str  |None =None
    #rating : float  |None =None | again , driver should not able to update rating for him self , so the default raing will be 0 , and a separate end point will created for updateing rating for the driver by passengers
    # car_id:int |None =None | updateing by making update on api/cars/{id}  , 

class DriverList(SQLModel):
    data: list[Driver]
    count: int