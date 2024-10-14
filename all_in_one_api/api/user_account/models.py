from api.database import Base
from sqlalchemy import JSON, Column,Integer,Text

class user_account(Base):
    __tablename__ = 'tbluser_account'

    id = Column(Integer,primary_key=True,index=True)
    hrms_id = Column(Text)
    username = Column(Text)
    pword = Column(Text)
    is_active = Column(Text)
    access_type = Column(Text)

class user_account_data(Base):
    __tablename__ = 'user_account_data'

    id = Column(Integer,primary_key=True,index=True)
    hrms_id = Column(Integer)
    full_name = Column(Text)
    emp_position = Column(Text)
    username = Column(Text)
    pword = Column(Text)
    is_active = Column(Text)
    ismodified = Column(Text)
    access_type= Column(Text)
    spims_access_array = Column(JSON)
    ps_access_array = Column(JSON)


