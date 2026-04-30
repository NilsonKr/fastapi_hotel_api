from pydantic import BaseModel
from datetime import datetime


class GuestModel(BaseModel):
  name: str
  check_in_at: datetime
  check_out_at: datetime
  amount: int

  @property
  def total_amount(self):
    return self.amount