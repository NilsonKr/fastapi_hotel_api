from app.db import engine
from datetime import timedelta
from datetime import datetime
from sqlmodel import Session

from .locations import ALLOWED_LOCATIONS_ENUM
from app.models import Guest, Location

def create_sample_guests_with_locations(session: Session) -> list[Guest]:
  location_1  = Location(name='Bogotham', rate=80, city=ALLOWED_LOCATIONS_ENUM.Bogota)
  location_2  = Location(name='Villagod', rate=40, city=ALLOWED_LOCATIONS_ENUM.villa_de_leyva)
  
  guest_1 = Guest(name="Nilson", check_out_at=datetime.now() + timedelta(days=5), amount=10, location=location_1)
  guest_2 = Guest(name="Laura", check_out_at=datetime.now() + timedelta(days=3), amount=10, location=location_1)
  guest_3 = Guest(name="Pepito", check_out_at=datetime.now() + timedelta(days=4), amount=6, location=location_2)

  session.add_all([guest_1, guest_2, guest_3])

  session.commit()

  session.refresh(guest_1)
  session.refresh(guest_2)
  session.refresh(guest_3)

  return [guest_1, guest_2, guest_3]
