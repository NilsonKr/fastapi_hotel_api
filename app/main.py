from fastapi import FastAPI

from .routers import scripts, guests, locations

app = FastAPI()
app.include_router(guests.router)
app.include_router(scripts.router)
app.include_router(locations.router)


@app.get('/')
async def home():
  return {'Data': 'Happy fastapi coding from dockeeer'}