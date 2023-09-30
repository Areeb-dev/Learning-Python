import os
from sqlalchemy import create_engine,text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from urllib.parse import quote_plus
from dotenv import load_dotenv

load_dotenv()

db_host = os.getenv("HOST")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")

encoded_password = quote_plus(db_password)

DATABASE_URL = f"postgresql://{db_user}:{encoded_password}@{db_host}/postgres"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
