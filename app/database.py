from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings

DATABASE_USERNAME = settings.database_username
DATABASE_PASSWORD = settings.database_password
DATABASE_HOSTNAME = settings.database_hostname
DATABASE_PORT = settings.database_port
DATABASE_NAME = settings.database_name

# SQLALCHEMY_DATABASE_URL = "postgresql://postgres:nir%20singh@localhost/FastAPI"
SQLALCHEMY_DATABASE_URL = f"postgresql://{DATABASE_USERNAME}:{DATABASE_PASSWORD}@{DATABASE_HOSTNAME}:{DATABASE_PORT}/{DATABASE_NAME}"


engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Used to Connect the Postgress to the FastAPI
# Not in use currenltly
# import psycopg2
# from psycopg2.extras import RealDictCursor
# import time

# while True:
#     try:
#         conn = psycopg2.connect(host='localhost', database='FastAPI',
#                                 user='postgres', password='nir singh', cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print("database connection was sucessful")
#         break
#     except Exception as error:
#         print("connection to database failed")
#         print("Error", error)
#         time.sleep(10)
