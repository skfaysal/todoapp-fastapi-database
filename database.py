from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

POSTGRES_DATABASE_URL = 'postgresql://postgres:faysal1997@localhost/TodoApplicationDatabase'

# This is for sqllite
# engine = create_engine(POSTGRES_DATABASE_URL, connect_args={'check_same_thread': False})

engine = create_engine(POSTGRES_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
