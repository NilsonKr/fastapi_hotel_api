from sqlmodel import select
from zoneinfo import ZoneInfo
from datetime import datetime 
from fastapi import APIRouter, HTTPException, Query
from typing import Annotated

from ..models import Guest,GuestBase, GuestPatch, APIResponse
from ..db import SessionDep

from ..utils.timezones import ALLOWED_ISO_ENUM, tz_by_iso

router = APIRouter(
  prefix='/guest',
  tags=['guest'],
  responses={404: {'description': 'Not found'}},
)

@router.get('/', response_model=APIResponse[list[Guest]], status_code=200)
async def register_guest(session: SessionDep, limit: Annotated[int, Query()] = 0, offset: Annotated[int, Query()] = 0):
  guests_from_db = session.exec(select(Guest).offset(offset).limit(limit))
  return {'detail':'creation success', 'data': guests_from_db.all()}



@router.post('/', response_model=APIResponse[Guest],status_code=201)
async def register_guest(guest_data: GuestBase, session: SessionDep):
  new_guest = guest_data 
  
  session.add(new_guest)
  session.commit()
  session.refresh(new_guest)

  return {'detail':'creation success', 'data': new_guest}


@router.patch('/{guest_id}')
async def patch_guest(guest_id: int, guest_data: GuestPatch, session: SessionDep):
  if not guest_data:
    raise HTTPException(status_code=400, detail='Payload is empty')

  print(guest_data, 'PATCH ADATAAAAA')

  guest_db = session.get(Guest, guest_id) 
  if not guest_db:
    raise HTTPException(status_code=404, detail='Guest not found')
  
  guest_db.sqlmodel_update(guest_data.model_dump(exclude_unset=True))

  session.add(guest_db)
  session.commit()
  session.refresh(guest_db)

  return {'detail':'updated success', 'data': guest_db}

@router.delete('/{guest_id}', status_code=200, response_model=APIResponse[Guest])
async def delete_guest(guest_id: int, session: SessionDep):
  guest_db = session.get(Guest, guest_id)

  if not guest_db:
    raise HTTPException(status_code=404, detail='Guest not found')

  session.delete(guest_db)
  session.commit()

  return {'detail': 'deleted success', 'data': guest_db}

@router.get('/date/{iso_code}')
async def getDate(iso_code: ALLOWED_ISO_ENUM):
  iso_tz = tz_by_iso.get(iso_code)
  tz = ZoneInfo(iso_tz)
  return {'date': datetime.now(tz).strftime('%Y-%m-%d %I:%M %p')}

  return {'status':'guest sample create', }