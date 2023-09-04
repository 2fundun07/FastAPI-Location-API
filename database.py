from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import create_engine,text

connection_url = f"postgresql://myuser:password@localhost:5432/postgres"
engine = create_engine(connection_url)

SessionLocal = sessionmaker(engine)
Base = declarative_base()