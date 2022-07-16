from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# user = "postgres"
# password = "ycdc2021"
# host = "192.168.16.8"
# db = "postgres"
# port='5432'

user = "postgres"
password = "password"
host = "postgresql_db"
db = "post_db"
port='5432'

SQLALCHEMY_DATABASE_URL=f"postgresql://{user}:{password}@{host}:{port}/{db}"

engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()