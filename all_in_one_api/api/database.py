from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


'''Dummy'''
AIO_SQLALCHEMY_DATABASE_URL = "postgresql://postgres:agimntadmin@10.201.64.24/dball_in_one"

# AIO_SQLALCHEMY_DATABASE_URL = "postgresql://postgres:agimntadmin@35.240.133.99/dball_in_one"
# SPIS_SQLALCHEMY_DATABASE_URL = "postgresql://postgres:serveradmin@192.168.110.133/dball_in_one"

engine = create_engine(AIO_SQLALCHEMY_DATABASE_URL,pool_size=20, max_overflow=0,pool_recycle=300)
SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)

'''Spareparts Inventory Management System Connection'''
SPIMS_SQLALCHEMY_DATABASE_URL = "postgresql://postgres:agimntadmin@10.201.64.24/db_spps"
# SPIMS_SQLALCHEMY_DATABASE_URL = "postgresql://postgres:agimntadmin@35.240.133.99/db_spps"

engine1 = create_engine(SPIMS_SQLALCHEMY_DATABASE_URL,pool_size=20, max_overflow=0,pool_recycle=300)
SessionLocal_SPIMS = sessionmaker(autocommit=False,autoflush=False,bind=engine1)


'''Purchasing System Connection'''
PS_SQLALCHEMY_DATABASE_URL = "postgresql://postgres:agimntadmin@10.201.64.24/dbpurchasing"
# PS_SQLALCHEMY_DATABASE_URL = "postgresql://postgres:agimntadmin@35.240.133.99/dbpurchasing"

engine2 = create_engine(PS_SQLALCHEMY_DATABASE_URL,pool_size=20, max_overflow=0,pool_recycle=300)
SessionLocal_PS = sessionmaker(autocommit=False,autoflush=False,bind=engine2)






Base = declarative_base()