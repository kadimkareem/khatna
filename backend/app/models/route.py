# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring


 

 
from datetime import datetime
from typing import  Optional ,List
from sqlmodel import Field, SQLModel, Relationship ,Column,DateTime,func,JSON


class BaseRoute(SQLModel):
    start: float  | None = None
    end: float  | None = None
    path: List[str] |None=None



class Route(BaseRoute, table=True):
    id: int | None = Field(default=None, primary_key=True)
    path: List[str] = Field(sa_column=Column(JSON)) 

    driver_id: int |None = Field( default=None,foreign_key="driver.id", nullable=True,unique=True) # default = None in case we don't want to updae driver_id 
    driver: "Driver" = Relationship(back_populates="routes", sa_relationship_kwargs={'uselist': False},)
    trips:"Trip" = Relationship( back_populates='route')

    created_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), server_default=func.now()))
    updated_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now()))


#----------schema---------
class RouteCreate(SQLModel):
    start: float  
    end: float  
    path: List[str] | None=None


class RouteUpdate(SQLModel):
    start: float  | None = None
    end: float  | None = None
    path: List[str] | None=None

class RoutesOut(SQLModel):
    routes: list[Route]
    count:int