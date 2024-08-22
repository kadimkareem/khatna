from typing import Any

from fastapi import APIRouter, HTTPException
from sqlmodel import func, select

from app.api.deps import CurrentUser, SessionDep
from app.models .trip import Trip , TripCreate,TripUpdate,TripsList
from app.models.token import Message
router = APIRouter()


@router.get("/", response_model=TripsList)
def read_trips(
    session: SessionDep, current_user: CurrentUser, skip: int = 0, limit: int = 100
) -> Any:
    """
    Retrieve trips. only admin can fetch all
    """

    if current_user.is_superuser:
        statment = select(func.count()).select_from(Trip)
        count = session.exec(statment).one()
        statement = select(Trip).offset(skip).limit(limit)
        trips = session.exec(statement).all()
    else:
        statment = (
            select(func.count())
            .select_from(Trip)
            #.where(Trip.owner_id == current_user.id) #TODO
        )
        count = session.exec(statment).one()
        statement = (
            select(Trip)
            #.where(Trip.owner_id == current_user.id) #TODO
            .offset(skip)
            .limit(limit)
        )
        trips = session.exec(statement).all()

    return TripsList(trips=trips, count=count)


@router.get("/{id}", response_model=Trip)
def read_trip(session: SessionDep, current_user: CurrentUser, id: int) -> Any:
    """
    Get trip by ID.
    """
    trip = session.get(Trip, id)
    if not trip:
        raise HTTPException(status_code=404, detail="Trip not found")
    # if not current_user.is_superuser and (trip.owner_id != current_user.id):
    #     raise HTTPException(status_code=400, detail="Not enough permissions") #TODO
    return trip


@router.post("/", response_model=TripCreate)
def create_trip(
    *, session: SessionDep, current_user: CurrentUser, trip_in: TripCreate
) -> Any:
    """
    Create new trip.
    """
    trip = Trip.model_validate(trip_in)
    session.add(trip)
    session.commit()
    session.refresh(trip)
    return trip


@router.put("/{id}", response_model=TripUpdate)
def update_trip(
    *, session: SessionDep, current_user: CurrentUser, id: int, trip_in: TripUpdate
) -> Any:
    """
    Update an trip.
    """
    trip = session.get(Trip, id)
    if not trip:
        raise HTTPException(status_code=404, detail="Trip not found")
    if not current_user.is_superuser and (trip.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    update_dict = trip_in.model_dump(exclude_unset=True)
    trip.sqlmodel_update(update_dict)
    session.add(trip)
    session.commit()
    session.refresh(trip)
    return trip


@router.delete("/{id}")
def delete_trip(session: SessionDep, current_user: CurrentUser, id: int) -> Message:

    """
    Delete an trip.
    """
    trip = session.get(Trip, id)
    if not trip:
        raise HTTPException(status_code=404, detail="Trip not found")
    if not current_user.is_superuser and (trip.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    session.delete(trip)
    session.commit()
    return Message(message="Trip deleted successfully")


# get list of newarby trips
router.get("/location/{location_id}", response_model=TripsList)
def get_trips_by_location_id(session: SessionDep, location_id: int) -> Any:
    trips = session.exec(select(Trip).where(Trip.location_id == location_id)).all()
    return TripsList(trips=trips)

router.get("/driver/{driver_id}", response_model=TripsList)
#passenger post TripFilter

#passsenger choose trips 
#passgern update choosen trip by puts it's id  in the trip