from pydantic import BaseModel

class spims_access_add(BaseModel):
    access : str
    status : str
    branch : str
    department : str
    hrms_id : str

    class Config():
        orm_mode = True

class spims_access_update(BaseModel):
    access : str
    status : str
    branch : str
    department : str

    class Config():
        orm_mode = True

