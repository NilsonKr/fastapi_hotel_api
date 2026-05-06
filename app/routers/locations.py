from fastapi import APIRouter
from sqlmodel import select

from ..db import SessionDep
from ..models import Location, LocationBase, APIResponse 

router = APIRouter(
  prefix='/locations',
  tags=['locations'],
)

@router.get('/', status_code=200, response_model=APIResponse[list[Location]])
async def get_locations(session: SessionDep):
  locations_list = session.exec(select(Location)).all()
  return {'detail': 'location registered', 'data': locations_list}

@router.post('/', status_code=201, response_model=APIResponse[Location])
async def register_location(location_data: LocationBase, session: SessionDep):

  new_location = Location.model_validate(location_data) 

  session.add(new_location)
  session.commit()
  session.refresh(new_location)

  return {'detail': 'location registered', 'data': new_location}