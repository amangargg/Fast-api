from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg
from psycopg.rows import dict_row
import time
import os

SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")
# SQLALCHEMY_DATABASE_URL = 'postgresql+psycopg://postgres:amangarg@localhost/fastapi'

import os

SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")

if SQLALCHEMY_DATABASE_URL.startswith("postgresql://"):
    SQLALCHEMY_DATABASE_URL = SQLALCHEMY_DATABASE_URL.replace(
        "postgresql://",
        "postgresql+psycopg://",
        1
    )

engine = create_engine(SQLALCHEMY_DATABASE_URL)
 
SessionLocal = sessionmaker(autocommit=False, autoflush= False, bind = engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# while(True):
#     try:
#         conn= psycopg.connect(host='localhost',dbname='fastapi',user='postgres',password='amangarg',row_factory=dict_row)
#         cursor = conn.cursor()
#         print('suc')
#         break
#     except Exception as error:
#         print('fail')
#         print(error)
#         time.sleep(2)