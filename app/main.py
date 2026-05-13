from time import time
from fastapi import FastAPI, Request

from .routers import scripts, guests, locations, reservations

app = FastAPI()
app.include_router(guests.router)
app.include_router(scripts.router)
app.include_router(locations.router)
app.include_router(reservations.router)

@app.middleware('http')
async def time_middleware(request: Request, next_call):
  start_time = time()
  response = await next_call(request)
  end_time = time()

  total_time = end_time - start_time

  print(f'Request at {request.url} took {total_time:.4f} secs')
  return response


@app.get('/')
async def home():
  return {'Data': 'Happy fastapi coding from dockeeer'}