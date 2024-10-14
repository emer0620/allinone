from api.database import Base
from sqlalchemy import Column,Integer,Text

class employee_data(Base):
    __tablename__ = 'employee_list'

    emp_id = Column(Integer,primary_key=True,index=True)
    full_name = Column(Text)
    status = Column(Text)
    emp_position = Column(Text)
    department = Column(Text)
    location_assign = Column(Text)
    dept_code = Column(Text)