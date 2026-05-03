from db import engine
from fastapi import FastAPI
from datetime import datetime
from zoneinfo import ZoneInfo

from models import Guest

from db import get_db_session, create_tables

from utils.timezones import ALLOWED_ISO_ENUM, tz_by_iso
from utils.scripts import create_sample_guests

app = FastAPI(lifespan=create_tables)

@app.get('/')
async def home():
  return {'Data': 'Happy fastapi coding from dockeeer'}


@app.get('/date/{iso_code}')
async def getDate(iso_code: ALLOWED_ISO_ENUM):
  iso_tz = tz_by_iso.get(iso_code)
  tz = ZoneInfo(iso_tz)
  return {'date': datetime.now(tz).strftime('%Y-%m-%d %I:%M %p')}

@app.post('/guest', status_code=201)
async def register_guest(guest: Guest):
  return {'status':'success', 'result': guest}

@app.get('/scripts/guest_sample')
async def scripts_guest_sample():
  create_sample_guests()
  return {'status':'guest sample create', }

if __name__ == '__main__':
  print('MAIN')