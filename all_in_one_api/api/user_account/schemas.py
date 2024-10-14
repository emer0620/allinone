from pydantic import BaseModel

class user_account_create(BaseModel):
    hrms_id : str
    username : str
    password : str
    is_active : str
    access_type : str
    
    class Config():
        orm_mode = True

class user_account_update(BaseModel):
    access_type : str
    is_active : str
    access_type : str

    class Config():
        orm_mode = True


