from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import create_engine,text

connection_url = f"postgresql://postgres:mysecretpassword@172.17.0.2:5432/postgres"
engine = create_engine(connection_url)

SessionLocal = sessionmaker(engine)
Base = declarative_base()