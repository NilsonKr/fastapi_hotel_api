from fastapi import APIRouter

from ..models import Guest, APIResponse
from ..db import SessionDep
from app.utils.scripts import create_sample_guests_with_locations

router = APIRouter(
  prefix='/script',
  tags=['scripts'],
)

@router.get('/guest_sample', response_model=APIResponse[list[Guest]])
async def scripts_guest_sample(session: SessionDep ):
  samples = create_sample_guests_with_locations(session)
  return {'detail': 'samples created', 'data': samples}