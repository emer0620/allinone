from pydantic import BaseModel

class user_access_add(BaseModel):
    access_branch : str
    access_dept : str
    access_role : str
    hrms_id : str
    status : str

    class Config():
        orm_mode = True

class user_access_update(BaseModel):
    access_branch : str
    access_dept : str
    access_role : str
    status : str

    class Config():
        orm_mode = True


class user_account_create(BaseModel):
    hrms_id: int
    employee_name : str
    position : str
    dept_code : str
    username : str
    pword : str
    branch : str
    added_by : str

    class Config():
        orm_mode = True

class user_account_update(BaseModel):
    username: str
    pword : str
    _isactive : str
    _ispasswordchanged : str

    class Config():
        orm_mode = True