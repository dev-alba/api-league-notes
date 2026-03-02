from fastapi import FastAPI
from fastapi.responses import JSONResponse
from exceptions import LeagueNotesException
from routers import notes_routers, users_routers, profiles_routers, champions_routers, auth_routers
from database import Base, engine
from models import champions_models, users_models, profiles_models, notes_models

app=FastAPI()
Base.metadata.create_all(bind=engine)

app.include_router(auth_routers.auth_router)
app.include_router(notes_routers.note_router)
app.include_router(users_routers.user_router)
app.include_router(profiles_routers.profile_router)
app.include_router(champions_routers.champion_router)

@app.exception_handler(LeagueNotesException)
async def invalid_credentials_handler(request, exc: LeagueNotesException):
    return JSONResponse(
        status_code=exc.status_code,
        content={'detail': exc.message})

@app.get('/')
def root():
    return {'message': 'Hello World'}
 