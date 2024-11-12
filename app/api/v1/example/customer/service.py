from app.api.base.service import BaseService
from app.api.v1.example.customer.repository import get_users, create_user, get_user_by_username
from app.api.v1.example.customer.schema import CustomerRq
from app.third_parties.db.models.customer.model import Customer
from app.utils import error_messages as ms


class UserService(BaseService):
    async def create_user(self, user_rq: CustomerRq):
        user = self.call_repos(await get_user_by_username(session=self.session, username=user_rq.username))
        if user:
            return self.response_exception(
                msg=ms.USER_ALREADY_EXIST,
                loc=self.create_user.__name__
            )

        user = Customer(
            username=user_rq.username,
            full_name=user_rq.fullname,
            email=user_rq.email,
            phone=user_rq.phone,
            gender=user_rq.gender,
        )

        _ = self.call_repos(await create_user(user=user, session=self.session))
        return self.response(data="Create user success")

    async def get_users(self):
        users = self.call_repos(await get_users(session=self.session))
        return self.response(data=users)
