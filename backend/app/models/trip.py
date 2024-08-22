
from datetime import datetime
from enum import Enum
from typing import List, Optional
from app.models.passenger import Passenger
from app.models.route import Route
from sqlmodel import Field, SQLModel, Relationship ,Column,DateTime,func
 


class TripType(str, Enum):
    daily = "daily"
    weekly = "weekly"
    monthly = "monthly"
    yearly = "yearly"   

 
class TripStatus(str, Enum):
    start="start"
    in_way="in_way"
    arrive_you="arrive_you"
    cancelled="cancelled"
    arrived_destination="arrived_destination"

class TripBase(SQLModel):
    estimation :Optional[datetime] =None
    cost :Optional[float] =None
    trip_status:Optional[TripStatus] =None
    type:Optional[TripType] =None
    passengers_count:Optional[int] =None
  

class Trip(TripBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    driver_id: int | None = Field(default=None, foreign_key="driver.id", nullable=False, unique=True)
    driver: "Driver" = Relationship(back_populates="trips")

    passenger_id: int | None = Field(default=0, foreign_key="passenger.id", nullable=True, unique=True)
    passengers: list["Passenger"] = Relationship(back_populates="trips")

    route_id: int | None = Field(default=None, foreign_key="route.id", nullable=False, unique=True)
    route: "Route" = Relationship(back_populates="trips")

    car_id: int | None = Field(default=None, foreign_key="car.id", nullable=False, unique=True)
    car: "Car" = Relationship(back_populates="trips")

    # attendances: list["Attendance"] = Relationship(back_populates="trip")

    created_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), server_default=func.now()))
    updated_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now()))



#---------schema------------
class TripCreate(SQLModel):
    # driver: "Driver" 
    # passengers:List["Passenger"] 
    route_id:int #just assing route_id
    car_id:int #just assing car_id 
    estimation : datetime 
    cost : float 
    tripStatus:TripStatus 
    type:TripType 
    passengers_count:Optional[int] =None
    passengers:List["Passenger"] | None = None #in case the driver own some passengers



class TripUpdate(SQLModel):
    # driver: "Driver" | None = None
    # passengers:List["Passenger"] | None = None
    # route: "Route" | None = None
    # car: "Car" | None = None
    route_id:int| None = None #just assing route_id
    car_id:int| None = None #just assing car_id 
    estimation : datetime | None = None
    cost : float | None = None
    tripStatus:TripStatus | None = None
    type:TripType | None = None
    passengers:List["Passenger"] | None = None
    passengers_count:Optional[int] =None



class TripsList(SQLModel):
    trips: List[Trip]
    count:int | None = None



class TripFilter(SQLModel):
    estimation :Optional[datetime] =None
    cost :Optional[float] =None
    trip_status:Optional[TripStatus] =None
    type:Optional[TripType] =None


