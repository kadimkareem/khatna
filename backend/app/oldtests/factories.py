import factory
from factory import fuzzy
from datetime import datetime
from app.models.car import Car, CarType
from app.models.driver import Driver
from app.models.passenger import Passenger, PassengerType
from app.models.route import Route
from app.models.trip import Trip, TripStatus, TripType
from app.models.user import User
from app.models.item import Item


from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.core.config import settings


engine = create_engine(str(settings.SQLALCHEMY_DATABASE_URI))

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class UserFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = User
        sqlalchemy_session = SessionLocal
    
    email = factory.Faker('email')
    is_active = True
    is_superuser = False
    full_name = factory.Faker('name')
    hashed_password = factory.Faker('password')

class DriverFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Driver
        sqlalchemy_session = SessionLocal

    license_number = factory.Faker('license_plate')
    license_expiry_date = factory.Faker('future_date')
    years_of_experience = factory.Faker('random_int', min=1, max=30)
    discription = factory.Faker('text')
    rating = factory.fuzzy.FuzzyFloat(0.5)
    user = factory.SubFactory(UserFactory)

class CarFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:

        model = Car
        sqlalchemy_session = SessionLocal

    model = factory.Faker('word')
    license_plate = factory.Faker('license_plate')
    year = factory.Faker('year')
    color = factory.Faker('color')
    photo = factory.Faker('image_url')
    capacity = factory.Faker('random_int', min=1, max=8)
    type = fuzzy.FuzzyChoice(CarType)
    driver = factory.SubFactory(DriverFactory)

class PassengerFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Passenger
        sqlalchemy_session = SessionLocal

    type = fuzzy.FuzzyChoice(PassengerType)
    location = factory.Faker('address')
    distination = factory.Faker('address')
    payment_method = factory.Faker('credit_card_provider')
    pickup_date = factory.Faker('future_date')
    pickup_time = factory.Faker('time')
    pickup_location = factory.Faker('address')
    return_date = factory.Faker('future_date')
    return_time = factory.Faker('time')
    service_hours = factory.Faker('random_int', min=1, max=24)
    user = factory.SubFactory(UserFactory)

class RouteFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Route
        sqlalchemy_session = SessionLocal

    start = factory.Faker('latitude')
    end = factory.Faker('longitude')
    path = factory.LazyAttribute(lambda _: [factory.Faker('address') for _ in range(5)])
    driver = factory.SubFactory(DriverFactory)

class TripFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Trip
        sqlalchemy_session = SessionLocal

    estimation = factory.Faker('future_datetime')
    cost = factory.fuzzy.FuzzyFloat(5,100)
    trip_status = fuzzy.FuzzyChoice(TripStatus)
    type = fuzzy.FuzzyChoice(TripType)
    passengers_count = factory.Faker('random_int', min=1, max=5)
    driver = factory.SubFactory(DriverFactory)
    route = factory.SubFactory(RouteFactory)
    car = factory.SubFactory(CarFactory)
    passengers = factory.SubFactory(PassengerFactory, factory_related_name='trips', size=3)

class ItemFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Item
        sqlalchemy_session = SessionLocal

    title = factory.Faker('word')
    description = factory.Faker('sentence')
    owner = factory.SubFactory(UserFactory)
