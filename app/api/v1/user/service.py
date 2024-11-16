from app.api.base.oauth import encode_jwt
from app.api.base.repository import auto_commit
from app.api.base.schema import Authentication
from app.api.base.service import BaseService
from app.api.v1.user.repository import get_users, create_user, get_user_by_username, get_roles_permissions_by_user_id, \
    get_user_by_id
from app.api.v1.user.schema import UserRq, ChangePasswordRq
from app.third_parties.db.models.model import User
from app.utils import error_messages as ms
from app.utils.functions import verify_password, hash_password
from app.utils.constant import constant as c


class UserService(BaseService):
    async def me(self):
        user_id = self.current_user.user_id

        roles_permissions = self.call_repos(
            await get_roles_permissions_by_user_id(session=self.session, user_id=user_id))

        user = self.call_repos(await get_user_by_id(session=self.session, id=user_id))

        return self.response(data={
            "id": user.id,
            "username": user.username,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "email": user.email,
            "phone": user.phone,
            "is_admin": user.is_admin,
            "roles": list({role["role_name"] for role in roles_permissions}),
            "permissions": list({per["permission_name"] for per in roles_permissions})
        })

    async def login(self, user: Authentication):
        user_db = self.call_repos(await get_user_by_username(session=self.session, username=user.username))
        if not user_db:
            return self.response_exception(
                msg=ms.USER_IS_NOT_EXIST,
                loc=self.login.__name__
            )

        if not verify_password(user.password, user_db.password):
            return self.response_exception(
                msg=ms.PASSWORD_INVALID,
                loc=self.login.__name__
            )

        user_info = {
            "user_id": user_db.id,
            "username": user_db.username,
            "first_name": user_db.first_name,
            "last_name": user_db.last_name,
            "email": user_db.email,
            "is_admin": user_db.is_admin
        }

        status, token, exp = await encode_jwt(
            data=user_info,
            minutes=c.ACCESS_TOKEN_EXPIRE_1_DAY,
            secret_key=c.SECRET_KEY,
            algorithm=c.ALGORITHM,
            token_type="access_token"
        )

        if not status:
            return self.response_exception(
                msg=ms.LOGIN_ERROR,
                detail=token,
                loc=self.login.__name__
            )

        _, refresh_token, _ = await encode_jwt(
            data=user_info,
            minutes=c.ACCESS_TOKEN_EXPIRE_1_DAY * 365,
            secret_key=c.SECRET_KEY,
            algorithm=c.ALGORITHM,
            token_type="refresh_token"
        )

        data = {
            "access_token": token,
            "refresh_token": refresh_token,
            "expire": int(exp.timestamp()),
        }

        return self.response(data=data)

    async def create_user(self, user_rq: UserRq):
        user = self.call_repos(await get_user_by_username(session=self.session, username=user_rq.username))
        if user:
            return self.response_exception(
                msg=ms.USER_ALREADY_EXIST,
                loc=self.create_user.__name__
            )

        user = User(
            username=user_rq.username,
            first_name=user_rq.first_name,
            last_name=user_rq.last_name,
            email=user_rq.email,
            phone=user_rq.phone,
            gender=user_rq.gender,
            password=hash_password(user_rq.password)
        )

        _ = self.call_repos(await create_user(user=user, session=self.session))
        return self.response(data={
            "id": user.id,
            "username": user.username,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "email": user.email,
            "phone": user.phone,
            "is_admin": user.is_admin
        })

    async def get_users(self):
        users = self.call_repos(await get_users(session=self.session))
        return self.response(data=users)

    async def change_password(self, p: ChangePasswordRq):
        user = self.call_repos(await get_user_by_username(session=self.session, username=self.current_user.username))
        if not user:
            return self.response_exception(
                msg=ms.USER_IS_NOT_EXIST,
                loc=self.change_password.__name__
            )

        if not verify_password(p.old_password, user.password):
            return self.response_exception(
                msg=ms.PASSWORD_INVALID,
                loc=self.change_password.__name__
            )

        new_password = hash_password(p.new_password)
        user.password = new_password

        self.session.commit()

        return self.response(data={"message": "Password updated successfully"})
