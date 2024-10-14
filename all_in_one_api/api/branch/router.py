from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from . import crud
import api.auth as auth

branch_router = APIRouter(
    prefix = '/Branch',
    tags = ['Branch']
)

@branch_router.get('/List')
async def branch_list(db:Session=Depends(auth.get_db)):
    return await crud.branch_list(db)