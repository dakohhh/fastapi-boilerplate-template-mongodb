from fastapi import FastAPI, Request

from .settings import settings

app = FastAPI(title=settings.APP_NAME, version="0.1.0")


@app.get("/")
async def root(requeest: Request):
    return {"setting": settings.APP_NAME}