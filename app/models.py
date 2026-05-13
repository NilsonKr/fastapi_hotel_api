from typing import Generic, TypeVar
from sqlmodel import SQLModel, Field, Relationship
from pydantic import BaseModel
from datetime import datetime

from app.utils.locations import ALLOWED_LOCATIONS_ENUM
from app.utils.reservations import RESERVATIONS_STATUS_ENUM

T = TypeVar('T')

class APIResponse(BaseModel, Generic[T]):
  detail: str
  data: T


class Reservation(SQLModel, table=True):
  id: int | None = Field(default=None, primary_key=True)
  guest_id: int = Field(foreign_key='guest.id')
  location_id: int = Field(foreign_key='location.id')
  status: RESERVATIONS_STATUS_ENUM = RESERVATIONS_STATUS_ENUM.CONFIRMED

  guest: 'Guest' = Relationship(back_populates='guest_reservations')
  location: 'Location' = Relationship(back_populates='location_reservations')

class ReservationPatch(BaseModel):
  status: RESERVATIONS_STATUS_ENUM

class GuestBase(SQLModel):
  name: str
  check_in_at: datetime = datetime.now()
  check_out_at: datetime
  amount: int
  
  @property
  def total_amount(self):
    return self.amount
  
class GuestRead(GuestBase):
  guest_reservations: list[Reservation]

class GuestPatch(GuestBase):
  name: str | None = None
  check_in_at: datetime | None = None
  check_out_at: datetime | None = None
  amount: int | None = None

class Guest(GuestBase, table=True):
  id: int | None = Field(default=None, primary_key=True)
  guest_reservations: list[Reservation] = Relationship(back_populates='guest')



class LocationBase(SQLModel):
  name: str 
  city: ALLOWED_LOCATIONS_ENUM = ALLOWED_LOCATIONS_ENUM.Bogota
  rate: int 

class Location(LocationBase, table=True):
  id: int | None = Field(default=None, primary_key=True)
  location_reservations: list[Reservation] = Relationship(back_populates='location')