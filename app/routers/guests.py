from zoneinfo import ZoneInfo
from datetime import datetime 
from fastapi import APIRouter

from ..models import Guest

from ..utils.timezones import ALLOWED_ISO_ENUM, tz_by_iso

router = APIRouter(
  prefix='/guest',
  tags=['guest'],
  responses={404: {"description": "Not found"}},
)

@router.post('/', status_code=201)
async def register_guest(guest: Guest):
  return {'status':'success', 'result': guest}


@router.get('/date/{iso_code}')
async def getDate(iso_code: ALLOWED_ISO_ENUM):
  iso_tz = tz_by_iso.get(iso_code)
  tz = ZoneInfo(iso_tz)
  return {'date': datetime.now(tz).strftime('%Y-%m-%d %I:%M %p')}

  return {'status':'guest sample create', }