from typing import Any

from app.models.passenger import Passenger
from fastapi import APIRouter, HTTPException
from sqlmodel import func, select

from app.api.deps import CurrentUser, SessionDep
from app.models .driver import Driver,DriverCreate ,DriverUpdate ,DriverList
from app.models.token import Message
router = APIRouter()

@router.get("/", response_model=DriverList)
def read_drivers(
    session: SessionDep, current_user: CurrentUser, skip: int = 0, limit: int = 100
) -> Any:
    """
    Retrieve drivers.
    """

    if current_user.is_superuser:
        statment = select(func.count()).select_from(Driver)
        count = session.exec(statment).one()
        statement = select(Driver).offset(skip).limit(limit)
        drivers = session.exec(statement).all()
        drivers = session.exec(statement).all()

    return DriverList(data=drivers, count=count)


@router.get("/{id}", response_model=Driver)
def read_driver(session: SessionDep, current_user: CurrentUser, id: int) -> Any:
    """
    Get driver by ID.
    """
    driver = session.get(Driver, id,)
    if not driver:
        raise HTTPException(status_code=404, detail="Driver not found")
    # if not current_user.is_superuser and (driver.owner_id != current_user.id):
    #     raise HTTPException(status_code=400, detail="Not enough permissions") #TODO
    return driver


@router.post("/", response_model=DriverCreate)
def create_driver(
    *, session: SessionDep, current_user: CurrentUser, driver_in: DriverCreate
) -> Any:
    """
    Create new driver.
    """
    
    #TODO add middleware , only driver and super user can create driver
    driver = Driver.model_validate(driver_in)
    driver.user_id=current_user.id

    session.add(driver)
    session.commit()
    session.refresh(driver)
    return driver


@router.put("/{id}", response_model=DriverUpdate)
def update_driver(
    *, session: SessionDep, current_user: CurrentUser, id: int, driver_in: DriverUpdate
) -> Any:
    """
    Update an driver.
    """
      #TODO add middleware , only driver and super user can update driver
    driver = session.get(Driver, id)
    if not driver:
        raise HTTPException(status_code=404, detail="Driver not found")
    if  current_user.id!=driver.user_id:
        raise HTTPException(status_code=400, detail="Not enough permissions")
    update_dict = driver_in.model_dump(exclude_unset=True)
    driver.sqlmodel_update(update_dict)
    driver.user_id=current_user.id
    session.add(driver)
    session.commit()
    session.refresh(driver)
    return driver


@router.delete("/{id}")
def delete_driver(session: SessionDep, current_user: CurrentUser, id: int) -> Message:
    """
    Delete an driver.
    """
      #TODO add middleware , only driver and super user can delete driver
    driver = session.get(Driver, id)
    if not driver:
        raise HTTPException(status_code=404, detail="Driver not found")
    if not current_user.is_superuser and (driver.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    session.delete(driver)
    session.commit()
    return Message(message="Driver deleted successfully")


#update driver rating 
@router.put("/rating/{id}")
def update_driver_rating(
    *, session: SessionDep, current_user: CurrentUser, id: int, rating: float
) -> Any:
    """
    Update an driver rating. only passengers can update rating
    """
      #TODO add middleware , only passenger and super user can rate driver
    driver = session.get(Driver, id)
    passneger=session.get(Passenger,current_user.id)
   # the user should have passenger account
    if not driver:
        raise HTTPException(status_code=404, detail="Driver not found")
    if not passneger:
        raise HTTPException(status_code=400, detail="your not allowed to update rating")
    driver.rating = rating
    session.add(driver)
    session.commit()
    session.refresh(driver)
    return driver

#TODO create car before driver , cuz when we create car the driver id exists but when we create driver, car id doesn't exist
#solve this delma , by creating the car with driver creation in same time 
#for that i will remove car_id from driver column in database , cuze the car and drive conneted in car table already