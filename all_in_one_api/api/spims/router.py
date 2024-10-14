from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from . import crud
import api.auth as auth


spims_router = APIRouter(
    prefix='/SPIMS',
    tags=['Spareparts Inventory Management System']
)

@spims_router.get('/Access_Role_List')
async def access_role_list(db:Session=Depends(auth.get_db)):
    list_data = await crud.access_role_list(db)
    result = []

    for data in list_data:
        if data.access_role not in result:
            result.append(data.access_role)
    
    return result