from fastapi import FastAPI, Request
from .database import connect_to_mongo, disconnect_from_mongo

from .settings import settings



app = FastAPI(title=settings.APP_NAME, version="0.1.0")


@app.on_event("startup")
async def startup_event():
    print("Starting up...")
    await connect_to_mongo()



@app.on_event("shutdown")
async def shutdown_event():
    print("Shutting down...")
    await disconnect_from_mongo()


@app.get("/")
async def root(requeest: Request):
    return {"setting": settings.APP_NAME}