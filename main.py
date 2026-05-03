from fastapi import FastAPI
from datetime import datetime
from zoneinfo import ZoneInfo

from models import GuestModel

from utils.timezones import ALLOWED_ISO_ENUM, tz_by_iso


app = FastAPI()

@app.get('/')
async def home():
  return {'Data': 'Happy fastapi coding from dockeeer'}


@app.get('/date/{iso_code}')
async def getDate(iso_code: ALLOWED_ISO_ENUM):
  iso_tz = tz_by_iso.get(iso_code)
  tz = ZoneInfo(iso_tz)
  return {'date': datetime.now(tz).strftime('%Y-%m-%d %I:%M %p')}

@app.post('/guest', status_code=201)
async def register_guest(guest: GuestModel):
  return {'status':'success', 'result': guest}