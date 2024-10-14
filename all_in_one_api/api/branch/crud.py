from sqlalchemy.orm import Session
from . import models

async def branch_list(db:Session):
    return db.query(models.Branch).all()