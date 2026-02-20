from fastapi import FastAPI
from routers import notes_routers, users_routers, profiles_routers, champions_routers
from database import Base, engine
from models import champions_models, users_models, profiles_models, notes_models

app=FastAPI()
Base.metadata.create_all(bind=engine)

app.include_router(notes_routers.note_router)
app.include_router(users_routers.user_router)
app.include_router(profiles_routers.profile_router)
app.include_router(champions_routers.champion_router)

@app.get('/')
def root():
    return {'message': 'Hello World'}
 