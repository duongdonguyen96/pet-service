import logging

from sqlalchemy.orm import Session

from app.api.base.repository import ReposReturn
from app.third_parties.db.models.model import User, Role, Permission, UserRole, RolePermission


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


async def get_user_by_id(session: Session, id: str) -> ReposReturn:
    try:
        user = session.query(
            User
        ).filter(
            User.id == id
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


async def get_roles_permissions_by_user_id(session: Session, user_id: str) -> ReposReturn:
    try:
        roles_permissions = session.query(
            Role.name.label('role_name'),
            Role.id.label('role_id'),
            Permission.name.label('permission_name'),
            Permission.id.label('permission_id')
        ).filter(
            UserRole.role_id == Role.id
        ).filter(
            Role.id == RolePermission.role_id
        ).filter(
            RolePermission.permission_id == Permission.id
        ).filter(
            UserRole.user_id == user_id
        ).all()

    except Exception as ex:
        logging.error(str(ex))
        return ReposReturn(msg=str(ex), is_error=True)

    return ReposReturn(data=roles_permissions)
