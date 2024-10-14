from sqlalchemy.orm import Session
from . import models

async def employee_per_id(db:Session,emp_id:str):
    return db.query(models.employee_data).filter(models.employee_data.emp_id==emp_id).first()

async def generate_employee_list(db:Session):
    return db.query(models.employee_data).all()
