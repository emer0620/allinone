from sqlalchemy.orm import Session
from . import models,schemas

async def access_role_list(db:Session):
    return db.query(models.spims_access_module_list).all()

async def access_role_added(db:Session,add_access:schemas.spims_access_add):
    dbadd = models.spims_user_access(
        department = add_access.department,
        access = add_access.access,
        status = add_access.status,
        branch = add_access.branch,
        hrms_id = add_access.hrms_id
    )
    db.add(dbadd)
    db.commit()
    return dbadd

async def access_role_update(db:Session,update_access:schemas.spims_access_update,id:int):
    dbupdate = db.query(models.spims_user_access).filter(models.spims_user_access.id==id).first()
    dbupdate.status = update_access.status
    dbupdate.branch = update_access.branch
    dbupdate.department = update_access.department
    dbupdate.access = update_access.access
    db.commit()
    db.refresh(dbupdate)
    return dbupdate

