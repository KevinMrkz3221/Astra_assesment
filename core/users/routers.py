from fastapi import APIRouter
from fastapi.responses import JSONResponse


router = APIRouter()


@router.get('/', tags=['prueba'])
def prueba():
    return JSONResponse({'Hello' : 'World'}, status_code=200)