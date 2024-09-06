from fastapi import FastAPI
import importlib
import uvicorn 

from app.settings import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    debug=settings.DEBUG
)


settings.routers(app)
settings.middlewares(app)


if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)