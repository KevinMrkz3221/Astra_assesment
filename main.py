from fastapi import FastAPI
import importlib
import uvicorn 
import inspect

from app.settings import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    debug=settings.DEBUG
)

for router_path in settings.INSTALLED_ROUTERS:
    module = importlib.import_module(router_path)
    app.include_router(module.routes)

for middleware in settings.MIDDLEWARES:
    module = importlib.import_module(middleware)
    for name in dir(module):
        member = getattr(module, name)
    
    # Verificar si el miembro es una clase
    if inspect.isclass(member):
        print(f'Member name: {name}')

        app.add_middleware(name)


if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)