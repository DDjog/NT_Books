from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

PG_URL = "postgresql+psycopg2://postgres:NewTasks@localhost:5432/Books"
engine = create_engine(PG_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()