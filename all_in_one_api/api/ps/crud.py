import datetime
import hashlib
from sqlalchemy.orm import Session
from . import models,schemas


async def ps_access_list(db:Session):
    return db.query(models.ps_accss_list).all()

async def user_account_check(db:Session,id:int):
    return db.query(models.User_Account).filter(models.User_Account.id==id).first() 

async def user_account_create(db:Session,create:schemas.user_account_create):
    dbcreate = models.User_Account(
        hrms_id = create.hrms_id,
        employee_name = create.employee_name,
        position = create.position,
        dept_code = create.dept_code,
        username = hashlib.sha512(create.username.encode('utf-8')).hexdigest(),
        pword = hashlib.sha512(create.pword.encode('utf-8')).hexdigest(),
        branch = create.branch,
        added_by = create.added_by,
        added_date = datetime.now(),
        _isactive = '0',
        _ispasswordchanged = '0',
        deleted = '0'
    )
    db.add(dbcreate)
    db.commit()
    db.refresh(dbcreate)
    return dbcreate

async def ps_user_access_add(db:Session,add_new:schemas.user_access_add):
    dbadd = models.ps_user_access(
        access_branch = add_new.access_branch,
        access_dept = add_new.access_dept,
        access_role = add_new.access_role,
        hrms_id = add_new.hrms_id,
        status = add_new.status
    )
    db.add(dbadd)
    db.commit()
    db.refresh(dbadd)
    return dbadd

async def ps_user_access_update(db:Session,update:schemas.user_access_update,id:int):
    dbupdate = db.query(models.ps_table_user_access).filter(models.ps_table_user_access.id==id).first()
    dbupdate.access_branch == update.access_branch
    dbupdate.access_dept = update.access_dept
    dbupdate.access_role = update.access_role
    dbupdate.status = update.status
    db.commit()
    db.refresh(dbupdate)
    return dbupdate
