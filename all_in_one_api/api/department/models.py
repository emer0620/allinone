from api.database import Base
from sqlalchemy import Column,Integer,Text

class Department(Base):
    __tablename__ = 'local_tbl_department'

    dept_id = Column(Integer,primary_key=True,index=True)
    dept_code = Column(Text)
    department = Column(Text)
    branch = Column(Text)