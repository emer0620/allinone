from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from . import crud
import api.auth as auth

ps_router = APIRouter(
    prefix='/PS',
    tags=['Purchasing System']
)

@ps_router.get('/Access_List')
async def ps_access_list(db:Session=Depends(auth.get_db)):
    return await crud.ps_access_list(db)