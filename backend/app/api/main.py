from fastapi import APIRouter
from app.api.routes import items, login, route, user, utils ,trip ,driver ,cars,passenger
api_router = APIRouter()

api_router.include_router(login.router, tags=["login"])
api_router.include_router(user.router, prefix="/users", tags=["users"])
api_router.include_router(utils.router, prefix="/utils", tags=["utils"])
api_router.include_router(items.router, prefix="/items", tags=["items"])
api_router.include_router(route.router, prefix="/routes", tags=["routes"])
api_router.include_router(trip.router, prefix="/trips", tags=["trips"])
api_router.include_router(driver.router, prefix="/drivers", tags=["drivers"])
api_router.include_router(cars.router, prefix="/cars", tags=["cars"])
api_router.include_router(passenger.router, prefix="/passengers", tags=["passengers"])


