from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
local = 'postgresql://123:123@localhost:5432/5'
produccion= 'postgres:XXXdb.elephantsql.com/rtfbexgf'

SQLALCHEMY_DATABASE_URL= 'postgresql:XXXclever-cloud.com:5432/b0ut1rrea0fgougw0lzq'

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(bind=engine,autocommit=False,autoflush=False)
Base= declarative_base()
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()
