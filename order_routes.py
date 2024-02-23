from fastapi import FastAPI, APIRouter

order_router = APIRouter()


@order_router.get('/order/')
async def hello():
    return {"message": "hello word"}
