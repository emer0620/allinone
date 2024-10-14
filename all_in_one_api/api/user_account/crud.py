import hashlib
from sqlalchemy.orm import Session
from . import schemas,models

async def user_account_check_hrms_id(db:Session,hrms_id:str):
    return db.query(models.user_account).filter(models.user_account.hrms_id == hrms_id).first()

async def user_account_list(db:Session):
    return db.query(models.user_account_data).all()

async def user_account_per_id(db:Session,id:int):
    return db.query(models.user_account_data).filter(models.user_account_data.id==id).first()

async def user_account_login(db:Session,username:str,password:str):
    return db.query(models.user_account).filter(models.user_account.username == hashlib.sha512(username.encode('utf-8')).hexdigest(),models.user_account.pword == hashlib.sha512(password.encode('utf-8')).hexdigest()).first()

async def user_account_add_new(db:Session,add_new:schemas.user_account_create):
    dbadd_new = models.user_account(
        hrms_id = add_new.hrms_id,
        username = hashlib.sha512(add_new.username.encode('utf-8')).hexdigest(),
        pword = hashlib.sha512(add_new.password.encode('utf-8')).hexdigest(),
        is_active =add_new.is_active,
        access_type = add_new.access_type
    )
    db.add(dbadd_new)
    db.commit()
    db.refresh(dbadd_new)
    return dbadd_new

async def user_account_update(db:Session,update:schemas.user_account_update,id:int):
    dbupdate = db.query(models.user_account).filter(models.user_account.id==id).first()
    # if update.username is not None:
    #     dbupdate.username = hashlib.sha512(update.username.encode('utf-8')).hexdigest()
    # if update.password is not None:
    #     dbupdate.pword = hashlib.sha512(update.password.encode('utf-8')).hexdigest()
    dbupdate.is_active = update.is_active
    dbupdate.access_type = update.access_type
    
    db.commit()
    db.refresh(dbupdate)
    return dbupdate

async def user_account_username_update(db:Session,username:str,id:int):
    dbuser = db.query(models.user_account).filter(models.user_account.id==id).first()
    dbuser.username = hashlib.sha512(username.encode('utf-8')).hexdigest()
    db.commit()
    db.refresh(dbuser)
    return dbuser


async def user_account_password_update(db:Session,pword:str,id:int):
    dbuser = db.query(models.user_account).filter(models.user_account.id==id).first()
    dbuser.pword = hashlib.sha512(pword.encode('utf-8')).hexdigest()
    db.commit()
    db.refresh(dbuser)
    return dbuser
