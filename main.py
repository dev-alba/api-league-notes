from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from core.exceptions import LeagueNotesException
from routers import (
    notes_routers,
    users_routers,
    profiles_routers,
    champions_routers,
    auth_routers,
    matchups_routers,
)
from core.database import Base, engine, session_maker
from models import (
    champions_models,
    matchups_models,
    users_models,
    profiles_models,
    notes_models,
)
from sqlalchemy import select
from scripts import import_champion
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)

    db = session_maker()
    try:
        from models.champions_models import Champion

        stmt = select(Champion).limit(1)
        exists = db.execute(stmt).scalar_one_or_none()
        if not exists:
            await import_champion.import_champions(db)
    finally:
        db.close()
    yield


app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # em produção troca pelo domínio do Firebase Hosting
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(auth_routers.auth_router)
app.include_router(notes_routers.note_router)
app.include_router(users_routers.user_router)
app.include_router(profiles_routers.profile_router)
app.include_router(champions_routers.champion_router)
app.include_router(matchups_routers.matchup_router)


@app.exception_handler(LeagueNotesException)
async def invalid_credentials_handler(request, exc: LeagueNotesException):
    return JSONResponse(status_code=exc.status_code, content={"detail": exc.message})


@app.get("/")
def root():
    return {"message": "Hello World"}
