import uuid
from datetime import date, datetime

from app.settings.config import TIME_ZONE

from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def today():
    """
    get today
    :return: date
    """
    return date.today()


def now():
    return datetime.now()


def get_current_time():
    return datetime.now(TIME_ZONE)


def generate_uuid() -> str:
    """
    :return: str
    """
    return uuid.uuid4().hex.upper()


def hash_password(password: str):
    return pwd_context.hash(password)


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)
