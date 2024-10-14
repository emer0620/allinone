from http.client import HTTPException
import secrets
from fastapi import Depends,status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from api.database import SessionLocal,SessionLocal_SPIMS,SessionLocal_PS

security = HTTPBasic()
def get_current_username(credentials:HTTPBasicCredentials=Depends(security)):
    correct_username = secrets.compare_digest(credentials.username,'agi-dev')
    correct_password = secrets.compare_digest(credentials.password,'1234')
    if not (correct_username and correct_password):
        raise HTTPException(
            status_code = status.HTTP_401_UNAUTHORIZED,
            details = 'Incorrect username and password',
            headers = {'WWW-Authenticate' : 'Basic'}
        )
    return credentials.username

def get_db(username:str=Depends(get_current_username)):
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_db_spims(username:str=Depends(get_current_username)):
    db=SessionLocal_SPIMS()
    try:
        yield db
    finally:
        db.close()

def get_db_ps(username:str=Depends(get_current_username)):
    db=SessionLocal_PS()
    try:
        yield db
    finally:
        db.close()
