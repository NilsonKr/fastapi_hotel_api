from app.db import engine
from datetime import timedelta
from datetime import datetime
from sqlmodel import Session

from app.models import Guest

def create_sample_guests(session: Session) -> list[Guest]:
  guest_1 = Guest(name="Nilson", check_out_at=datetime.now() + timedelta(days=5), amount=10)
  guest_2 = Guest(name="Laura", check_out_at=datetime.now() + timedelta(days=3), amount=10)
  guest_3 = Guest(name="Pepito", check_out_at=datetime.now() + timedelta(days=4), amount=6)

  session.add_all([guest_1, guest_2, guest_3])

  session.commit()

  session.refresh(guest_1)
  session.refresh(guest_2)
  session.refresh(guest_3)

  return [guest_1, guest_2, guest_3]


