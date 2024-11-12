import uuid
from datetime import date, datetime

from app.settings.config import TIME_ZONE


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
