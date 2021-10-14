from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# import os
#
# SQLALCHEMY_DATABASE_URL = os.environ['DATABASE_URL']
# print(SQLALCHEMY_DATABASE_URL)
#
# engine = create_engine(SQLALCHEMY_DATABASE_URL)

engine = create_engine("mysql+pymysql://root:1234Password@localhost:3306/mybd")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
