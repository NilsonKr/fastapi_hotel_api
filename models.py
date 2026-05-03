from sqlmodel import SQLModel, Field
from pydantic import BaseModel
from datetime import datetime

class GuestModel(SQLModel):
  name: str
  check_in_at: datetime = datetime.now()
  check_out_at: datetime
  amount: int

  @property
  def total_amount(self):
    return self.amount

class Guest(GuestModel, table=True):
  id: int | None = Field(default=None, primary_key=True)
