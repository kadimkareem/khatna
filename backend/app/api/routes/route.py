from typing import Any

from app.models.driver import Driver
from fastapi import APIRouter, HTTPException
from sqlmodel import func, select

from app.api.deps import CurrentUser, SessionDep

from app.models.route import Route ,RoutesOut ,RouteCreate,RouteUpdate
from app.models.token import Message
router = APIRouter()



@router.get("/", response_model=RoutesOut)
def read_routes(
    session: SessionDep, current_user: CurrentUser, skip: int = 0, limit: int = 100
) -> Any:
    """
    Retrieve routes.
    """
    if current_user.is_superuser:
        statment = select(func.count()).select_from(Route)
        count = session.exec(statment).one()
        statement = select(Route).offset(skip).limit(limit)
        routes = session.exec(statement).all()

    else:
        raise HTTPException(status_code=400, detail="Not enough permissions")

    return RoutesOut(routes=routes, count=count)


@router.get("/{id}", response_model=Route)
def read_route(session: SessionDep, current_user: CurrentUser, id: int) -> Any:
    """
    Get route by ID. any one can get route
    """
    route = session.get(Route, id)
    if not route:
        raise HTTPException(status_code=404, detail="Route not found")
    return route


@router.post("/", response_model=RouteCreate)
def create_route(
    *, session: SessionDep, current_user: CurrentUser, route_in: RouteCreate
) -> Any:
    """
    Create new route.
    """
    driver=session.get(Driver,current_user.id)
    if current_user.is_superuser and current_user.id==driver.user_id :
        route = Route.model_validate(route_in)
        print(f'route is {route}')
        route.driver_id=current_user.id
        session.add(route)
        session.commit()
        session.refresh(route)
    return route


@router.put("/{id}", response_model=RouteUpdate)
def update_route(
    *, session: SessionDep, current_user: CurrentUser, id: int, route_in: RouteUpdate
) -> Any:
    """
    Update an route.
    """
    route = session.get(Route, id)
    if not route:
        raise HTTPException(status_code=404, detail="Route not found")
    if not current_user.is_superuser and (route.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    update_dict = route_in.model_dump(exclude_unset=True)
    route.sqlmodel_update(update_dict)
    session.add(route)
    session.commit()
    session.refresh(route)
    return route


@router.delete("/{id}")
def delete_route(session: SessionDep, current_user: CurrentUser, id: int) -> Message:
    """
    Delete an route.
    """
    route = session.get(Route, id)
    if not route:
        raise HTTPException(status_code=404, detail="Route not found")
    if not current_user.is_superuser and (route.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    session.delete(route)
    session.commit()
    return Message(message="Route deleted successfully")

@router.get("/near/{location}", )
def find_routes_near_location(session: SessionDep,location: str):
    # return crud.find_routes_near_location(db=db, location=location)
    return session.exec(select(Route).where(Route.distenation == location)).all()