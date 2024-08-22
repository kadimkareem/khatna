# from datetime import datetime
# from sqlmodel import Field, Relationship, SQLModel
# from app.models.passenger import Passenger
# from app.models.trip import Trip

# class BaseAttendance(SQLModel):
#     date: datetime | None = None
#     is_present: bool | None = None
#     trip_id: int | None = None
#     passenger_id: int | None = None

# class Attendance(BaseAttendance, table=True):
#     id: int = Field(default=None, primary_key=True, index=True, unique=True)
#     passenger_id: int | None = Field(default=None, foreign_key="passenger.id", nullable=False)
#     passenger: Passenger = Relationship(back_populates="attendances")

#     trip_id: int | None = Field(default=None, foreign_key="trip.id", nullable=False)
#     trip: Trip = Relationship(back_populates="attendances")

# class AttendanceCreate(SQLModel):
#     date: datetime
#     is_present: bool
#     trip_id: int
#     passenger_id: int

# class AttendanceUpdate(SQLModel):
#     date: datetime | None = None
#     is_present: bool | None = None
