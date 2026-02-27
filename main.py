from fastapi import FastAPI
from fastapi.responses import JSONResponse
from excepctions import InvalidCredentials, UserNotFound, UserAlreadyExists, UserCannotBeDeleted, ProfileNotFound, ProfilesNotFound, ProfileAlreadyExists, ProfileCannotBeDeleted, NoteNotFound, NotesNotFound
from routers import notes_routers, users_routers, profiles_routers, champions_routers
from database import Base, engine
from models import champions_models, users_models, profiles_models, notes_models

app=FastAPI()
Base.metadata.create_all(bind=engine)

app.include_router(notes_routers.note_router)
app.include_router(users_routers.user_router)
app.include_router(profiles_routers.profile_router)
app.include_router(champions_routers.champion_router)

@app.exception_handler(InvalidCredentials)
async def invalid_credentials_handler(request, exc):
    return JSONResponse(
        status_code=403, content={'detail': exc.message})

#       USER HANDLERS
@app.exception_handler(UserNotFound)
async def user_not_found_handler(request, exc):
    return JSONResponse(
        status_code=404, content={'detail': exc.message})

@app.exception_handler(UserAlreadyExists)
async def user_already_exists_handler(request, exc):
    return JSONResponse(
        status_code=409, content={'detail': exc.message})

@app.exception_handler(UserCannotBeDeleted)
async def user_cannot_be_deleted_handler(request, exc):
    return JSONResponse(
        status_code=409, content={'detail': exc.message})

#       PROFILE HANDLERS
@app.exception_handler(ProfileNotFound)
async def profile_not_found_handler(request, exc):
    return JSONResponse(
        status_code=404, content={'detail': exc.message})

@app.exception_handler(ProfilesNotFound)
async def profiles_not_found_handler(request, exc):
    return JSONResponse(
        status_code=404, content={'detail': exc.message})

@app.exception_handler(ProfileAlreadyExists)
async def profile_already_exists_handler(request, exc):
    return JSONResponse(
        status_code=409, content={'detail': exc.message})

@app.exception_handler(ProfileCannotBeDeleted)
async def profile_cannot_be_deleted_handler(request, exc):
    return JSONResponse(
        status_code=409, content={'detail': exc.message})

#       NOTES HANDLERS
@app.exception_handler(NoteNotFound)
async def note_not_found_handler(request, exc):
    return JSONResponse(
        status_code=404, content={'detail': exc.message})

@app.exception_handler(NotesNotFound)
async def note_not_found_handler(request, exc):
    return JSONResponse(
        status_code=404, content={'detail': exc.message})

@app.get('/')
def root():
    return {'message': 'Hello World'}
 