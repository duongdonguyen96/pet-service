from dataclasses import dataclass
from typing import Any

from sqlalchemy.exc import SQLAlchemyError

from app.settings.config import logger


@dataclass
class ReposReturn:
    is_error: bool = False
    loc: str = ''
    msg: str = ''
    detail: str = ''
    data: Any = None


def auto_commit(func):
    async def wrapper(*args, **kwargs):
        print(kwargs)
        print(args)
        if 'session' not in kwargs:
            return ReposReturn(is_error=True, msg='', detail='can not found session in kwargs', loc=func.__name__)

        session = kwargs['session']
        try:
            result = await func(*args, **kwargs)
            if result.is_error:
                raise SQLAlchemyError(result.msg)

            session.commit()
            logger.info(f"Success calling db func: {func.__name__}")
            return result
        except SQLAlchemyError as ex:
            logger.error(ex.args)
            session.rollback()
            return ReposReturn(is_error=True, msg=str(ex.args) if ex.args else "ERROR_COMMIT", loc=func.__name__)

    return wrapper
