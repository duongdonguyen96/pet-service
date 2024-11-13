from sqlalchemy import VARCHAR, Column, DateTime, String, Boolean
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.settings.config import TIME_ZONE
from app.settings.database import DB_CONFIG
from app.utils.functions import generate_uuid, get_current_time

DATABASE_URL = URL.create(
    drivername="postgresql",
    username=DB_CONFIG['username'],
    password=DB_CONFIG['password'],
    host=DB_CONFIG['host'],
    port=DB_CONFIG['port'],
    database=DB_CONFIG['service_name']
)

engine = create_engine(
    DATABASE_URL,
    connect_args={"options": f"-c timezone={TIME_ZONE}"}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


class CustomBaseModel:
    id = Column(VARCHAR(32), name="id", primary_key=True, default=generate_uuid)
    updated_by = Column(VARCHAR(32))
    created_by = Column(VARCHAR(32))
    created_at = Column(DateTime, default=get_current_time)
    updated_at = Column(DateTime)
    is_active = Column(Boolean(), default=1)
