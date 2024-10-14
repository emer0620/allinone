from api.database import Base
from sqlalchemy import Column,Integer,Text

class Branch(Base):
    __tablename__ = 'local_tbl_branch'

    branch_id = Column(Integer,primary_key=True,index=True)
    branch = Column(Text)