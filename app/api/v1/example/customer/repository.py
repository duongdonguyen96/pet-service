import logging

from sqlalchemy.orm import Session

from app.api.base.repository import ReposReturn
from app.third_parties.db.models.customer.model import (Customer)


async def create_user(session: Session, user: Customer) -> ReposReturn:
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
            Customer
        ).filter(
            Customer.username == username
        ).first()

    except Exception as ex:
        logging.error(str(ex))
        return ReposReturn(msg=str(ex), is_error=True)

    return ReposReturn(data=user)


async def get_users(session: Session) -> ReposReturn:
    try:
        users = session.query(
            Customer.id,
            Customer.username,
            Customer.full_name,
            Customer.email,

        ).all()

    except Exception as ex:
        logging.error(str(ex))
        return ReposReturn(msg=str(ex), is_error=True)

    return ReposReturn(data=users)
