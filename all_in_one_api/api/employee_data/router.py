from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from . import crud
import api.auth as auth

employee_data_router = APIRouter(
    prefix = '/Employee_Data',
    tags = ['Employee Data']
)

@employee_data_router.get('/Per_ID')
async def employee_data_per_id(emp_id:int,db:Session=Depends(auth.get_db)):
    return await crud.employee_per_id(db,emp_id)
@employee_data_router.get('/List')
async def employee_data_list(db:Session=Depends(auth.get_db)):
    return await crud.generate_employee_list(db)