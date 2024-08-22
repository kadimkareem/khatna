


from enum import Enum
from sqlmodel import Field, SQLModel, Relationship   ,Column,DateTime,func
from datetime import datetime
from typing import Optional

class PassengerType(str, Enum):
    mail="maile"
    female="female"
    mix="mix"

class PassengerBase(SQLModel):
    type:PassengerType  | None = None
    location :str  | None = None
    distination :str  | None = None
    payment_method :str  | None = None
    pickup_date :datetime  | None = None
    pickup_time :datetime  | None = None
    pickup_location:str  | None = None
    return_date :datetime  | None = None
    return_time :datetime  | None = None
    service_hours :int  | None = None

class Passenger(PassengerBase, table=True):
    id: int = Field(default=None, primary_key=True, index=True, unique=True)
    user_id: int | None = Field(default=None, foreign_key="user.id", nullable=False, unique=True)
    user: "User" = Relationship(back_populates="passenger")

    trips: list["Trip"] = Relationship(back_populates="passengers")
    #attendances: list["Attendance"] = Relationship(back_populates="passenger")

    created_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), server_default=func.now()))
    updated_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now()))


#---------schema---------
class CreatePassenger(SQLModel):
    type:PassengerType 
    location :str 
    distination :str 
    payment_method :str 
    pickup_date :datetime 
    pickup_time :datetime 
    pickup_location:str 
    return_date :datetime 
    return_time :datetime 
    service_hours :int 
class UpdatePassenger(SQLModel):
    type:PassengerType  | None = None
    location :str  | None = None
    distination :str  | None = None
    payment_method :str  | None = None
    pickup_date :datetime  | None = None
    pickup_time :datetime  | None = None
    pickup_location:str  | None = None
    return_date :datetime  | None = None
    return_time :datetime  | None = None
    service_hours :int  | None = None

class PassengerList(SQLModel):
    passengers: list[Passenger] 
    count: int  