from api.database import Base
from sqlalchemy import Column,Integer,Text

class spims_access_module_list(Base):
    __tablename__ = 'local_tbl_spims_access_module_list'

    id = Column(Integer,primary_key=True,index=True)
    access_role = Column(Text)
    access = Column(Text)

class spims_user_access(Base):
    __tablename__ = 'tblusers'

    id = Column(Integer,primary_key=True,index=True)
    name = Column(Text)
    department = Column(Text)
    position = Column(Text)
    username = Column(Text)
    password = Column(Text)
    access = Column(Text)
    online = Column(Text)
    status = Column(Text)
    branch = Column(Text)
    skin_use = Column(Text)
    hash_username = Column(Text)
    hash_password = Column(Text)
    hrms_id = Column(Integer)      
