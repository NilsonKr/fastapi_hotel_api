from fastapi import APIRouter, HTTPException, Query
from typing import Annotated

from ..models import Guest, Location, Reservation,ReservationPatch, APIResponse
from ..db import SessionDep

router = APIRouter(
  prefix='/reservation',
  tags=['reservation'],
  responses={404: {'description': 'Not found'}},
)

@router.get('/{guest_id}', status_code=200, response_model=APIResponse[list[Reservation]])                   
async def get_guest_reservations(guest_id: int, session: SessionDep):                                                  
    guest = session.get(Guest, guest_id)                                                                            
    if not guest:
        raise HTTPException(status_code=404, detail='Guest not found')                                              
    return {'detail': 'success', 'data': guest.guest_reservations}

@router.post('/{guest_id}/{location_id}', status_code=201, response_model=APIResponse[Reservation])                   
async def add_guest_reservations(guest_id: int, location_id:int,session: SessionDep):                                                  
    guest = session.get(Guest, guest_id)
    location = session.get(Location, location_id)                                                                            
    
    if not guest or not location:
        raise HTTPException(status_code=404, detail='Guest not found')                                              
  
    new_reservation = Reservation(guest_id=guest_id, location_id=location_id)

    session.add(new_reservation)
    session.commit()
    session.refresh(new_reservation)

    return {'detail': 'success', 'data': new_reservation}

@router.patch('/{reservation_id}', status_code=201, response_model=APIResponse[Reservation])                   
async def update_reservation(reservation_id: int, reservation_data: ReservationPatch ,session: SessionDep):                                                  
    reservation = session.get(Reservation, reservation_id)

    if not reservation_data or not reservation:
        raise HTTPException(status_code=404, detail='Not reservation data')                                              

    reservation.sqlmodel_update(ReservationPatch.model_dump(exclude_unset=True))

    session.add(reservation)
    session.commit()
    session.refresh(reservation)

    return {'detail': 'success', 'data': reservation}