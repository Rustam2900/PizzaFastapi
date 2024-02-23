from fastapi import FastAPI, APIRouter

auth_router = APIRouter()


@auth_router.get('/auth/')
async def hello():
    return {"message": "Hello Word"}
