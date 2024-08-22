from typing import Any

from app.models.driver import Driver
from fastapi import APIRouter, HTTPException
from sqlmodel import func, select

from app.api.deps import CurrentUser, SessionDep
from app.models .car import Car ,CarOut ,CreateCar,UpdateCar ,CarsOut
from app.models.token import Message
router = APIRouter()


@router.get("/", response_model=CarsOut)
def read_cars(
    session: SessionDep, current_user: CurrentUser, skip: int = 0, limit: int = 100
) -> Any:
    """
    Retrieve cars.
    """

    if  current_user.is_superuser:
        statment = select(func.count()).select_from(Car)
        count = session.exec(statment).one()
        statement = select(Car).offset(skip).limit(limit)
        cars = session.exec(statement).all()
        cars = session.exec(statement).all()
        return Car(data=cars, count=count)
    else: 
        raise HTTPException(status_code=400, detail="Not enough permissions")


@router.get("/{id}", response_model=CarOut)
def read_car(session: SessionDep, current_user: CurrentUser, id: int) -> Any:
    """
    Get car by ID.
    """
    car = session.get(Car, id,)
    if not car:
        raise HTTPException(status_code=404, detail="Car not found")
    # if not current_user.is_superuser and (car.owner_id != current_user.id):
    #     raise HTTPException(status_code=400, detail="Not enough permissions") #TODO
    return car


@router.post("/", response_model=CreateCar)
def create_car(
    *, session: SessionDep, current_user: CurrentUser, create_car: CreateCar
) -> Any:
    """
    Create new car.
    """
    try:
        car=Car.model_validate(create_car)
        car.driver_id=current_user.id
        session.add(car)
        session.commit()
        session.refresh(car)
        return car
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    


@router.put("/{id}", response_model=UpdateCar,)
def update_car(
    *, session: SessionDep, current_user: CurrentUser, id: int, car_in: UpdateCar
) -> Car:
    """
    Update an car.
    """
    car = session.get(Car, id)
    driver=session.get(Driver,current_user.id) #TODO let the middleware do that and put driver id in request , so you fetch driver id in request and pass it here
    if not car:
        raise HTTPException(status_code=404, detail="Car not found")
    if not driver :
        raise HTTPException(status_code=400, detail="Not enough permissions")
    update_dict = car_in.model_dump(exclude_unset=True)
    update_dict
    car.sqlmodel_update(update_dict)
    car.driver_id=driver.id
    session.add(car)
    session.commit()
    session.refresh(car)
    return car


@router.delete("/{id}")
def delete_car(session: SessionDep, current_user: CurrentUser, id: int) -> Message:
    """
    Delete an car.
    """
    car = session.get(Car, id)
    if not car:
        raise HTTPException(status_code=404, detail="Car not found")
    if not current_user.is_superuser and (car.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    session.delete(car)
    session.commit()
    return Message(message="Car deleted successfully")
