from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
import api.auth as auth
from . import crud

department_router = APIRouter(
    prefix = '/Department',
    tags=['Department']
)

@department_router.get('/List')
async def department_list(db:Session=Depends(auth.get_db)):
    return await crud.department_list(db)