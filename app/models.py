from typing import Generic, TypeVar
from sqlmodel import SQLModel, Field
from pydantic import BaseModel
from datetime import datetime

T = TypeVar('T')

class APIResponse(BaseModel, Generic[T]):
  detail: str
  data: T

class GuestBase(SQLModel):
  name: str
  check_in_at: datetime = datetime.now()
  check_out_at: datetime
  amount: int
  
  @property
  def total_amount(self):
    return self.amount

class Guest(GuestBase, table=True):
  id: int | None = Field(default=None, primary_key=True)

class GuestPatch(GuestBase):
  name: str | None = None
  check_in_at: datetime | None = None
  check_out_at: datetime | None = None
  amount: int | None = None

