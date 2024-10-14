from sqlalchemy.orm import Session
from . import models

async def department_list(db:Session):
    return db.query(models.Department).all()
