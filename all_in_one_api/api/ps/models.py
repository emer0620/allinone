from api.database import Base
from sqlalchemy import TIMESTAMP, Column,Integer,Text

class ps_accss_list(Base):
    __tablename__ = 'local_tbl_ps_access_list'

    id = Column(Integer,primary_key=True,index=True)
    access_name = Column(Text)

class User_Account(Base):
    __tablename__ = 'tbluseraccount'

    id = Column(Integer,primary_key=True,index=True)
    hrms_id = Column(Integer)
    employee_name = Column(Text)
    position = Column(Text)
    dept_code = Column(Text)
    username = Column(Text)
    pword = Column(Text)
    branch = Column(Text)
    added_by = Column(Text)
    added_date = Column(TIMESTAMP)
    deleted = Column(Text)
    _isactive = Column(Text)
    _ispasswordchanged = Column(Text)

class ps_table_user_access(Base):
    __tablename__ = 'tbluser_access'

    id = Column(Integer,primary_key=True,index=True)
    user_id = Column(Integer)
    access_branch = Column(Text)
    access_dept = Column(Text)
    access_role = Column(Text)
    status = Column(Text)

class ps_user_access(Base):
    __tablename__ = 'user_access'

    id = Column(Integer,primary_key=True,index=True)
    user_id = Column(Integer)
    access_branch = Column(Text)
    access_dept = Column(Text)
    access_role = Column(Text)
    hrms_id = Column(Text)
    status = Column(Text)