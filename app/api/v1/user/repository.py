import logging

from sqlalchemy.orm import Session

from app.api.base.repository import ReposReturn
from app.third_parties.db.models.model import User


async def create_user(session: Session, user: User) -> ReposReturn:
    try:
        session.add(user)
        session.commit()
    except Exception as ex:
        logging.error(str(ex))
        return ReposReturn(msg=str(ex), is_error=True)

    return ReposReturn()


async def get_user_by_username(session: Session, username: str) -> ReposReturn:
    try:
        user = session.query(
            User
        ).filter(
            User.username == username
        ).first()

    except Exception as ex:
        logging.error(str(ex))
        return ReposReturn(msg=str(ex), is_error=True)

    return ReposReturn(data=user)


async def get_users(session: Session) -> ReposReturn:
    try:
        users = session.query(
            User.id,
            User.username,
            User.first_name,
            User.last_name,
            User.email,
            User.gender,
            User.is_admin
        ).all()

    except Exception as ex:
        logging.error(str(ex))
        return ReposReturn(msg=str(ex), is_error=True)

    return ReposReturn(data=users)
