from typing import Any

from fastapi import APIRouter, HTTPException
from sqlmodel import func, select

from app.api.deps import CurrentUser, SessionDep
from app.models .passenger import Passenger ,UpdatePassenger ,CreatePassenger,PassengerList
from app.models.token import Message
router = APIRouter()


@router.get("/", response_model=PassengerList)
def read_passengers(
    session: SessionDep, current_user: CurrentUser, skip: int = 0, limit: int = 100
) -> Any:
    """
    Retrieve passengers. only super user can fetch all
    """
#TODO add middleware only super user can fetch all
    if current_user is not None:
        statment = select(func.count()).select_from(Passenger)
        count = session.exec(statment).one()
        statement = select(Passenger).offset(skip).limit(limit)
        passengers = session.exec(statement).all()
        passengers = session.exec(statement).all()


    return PassengerList(passengers=passengers, count=count)


@router.get("/{id}", response_model=Passenger)
def read_passenger(session: SessionDep, current_user: CurrentUser, id: int) -> Any:
    """
    Get passenger by ID.
    """
      #TODO add middleware , any one can get passenger
    passenger = session.get(Passenger, id,)
    if not passenger:
        raise HTTPException(status_code=404, detail="Passenger not found")

    return passenger


@router.post("/", response_model=CreatePassenger)
def create_passenger(
    *, session: SessionDep, current_user: CurrentUser, passenger_in: CreatePassenger
) -> Any:
    """
    Create new passenger.
    """
      #TODO add middleware , only passenger and super user can create driver
    passenger = Passenger.model_validate(passenger_in)
    passenger.user_id=current_user.id

    session.add(passenger)
    session.commit()
    session.refresh(passenger)
    return passenger


@router.put("/{id}", response_model=UpdatePassenger)
def update_passenger(
    *, session: SessionDep, current_user: CurrentUser, id: int, passenger_in: UpdatePassenger
) -> Any:
    """
    Update an passenger.
    """
    passenger = session.get(Passenger, id)
    if not passenger:
        raise HTTPException(status_code=404, detail="Passenger not found")
    if not current_user.id!=passenger.user_id:
        raise HTTPException(status_code=400, detail="Not enough permissions")
    update_dict = passenger_in.model_dump(exclude_unset=True)
    passenger.sqlmodel_update(update_dict)
    session.add(passenger)
    session.commit()
    session.refresh(passenger)
    return passenger


@router.delete("/{id}")
def delete_passenger(session: SessionDep, current_user: CurrentUser, id: int) -> Message:
    """
    Delete an passenger.
    """
      #TODO add middleware , only passenger and super user can delete passenger
      #TODO add middleware ,check passenger id and pass it in the request 
    passenger = session.get(Passenger, id)
    if not passenger:
        raise HTTPException(status_code=404, detail="Passenger not found")
    if not current_user.is_superuser and (passenger.user_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    session.delete(passenger)
    session.commit()
    return Message(message="Passenger deleted successfully")


#join trip

#leave trip

#rate driver

#absent

#TODO create attendance report table in db