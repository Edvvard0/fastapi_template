import uvicorn
from fastapi import FastAPI
from starlette.staticfiles import StaticFiles

from app.config import settings
from app.users.router import router as user_router
from app.pages.router import router as pages_router


app = FastAPI()
app.include_router(user_router)
app.include_router(pages_router)

app.mount("/static", StaticFiles(directory="app/static"), "static")


if __name__ == "__main__":
    uvicorn.run("main:app", host=settings.API_HOST, port=settings.API_PORT)

