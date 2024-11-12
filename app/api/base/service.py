import logging
from typing import Optional

from sqlalchemy.orm import Session
from starlette import status

from app.api.base.except_custom import ExceptionHandle
from app.api.base.repository import ReposReturn
from app.api.base.schema import Error
from app.third_parties.db.base import SessionLocal


class BaseService:
    """
    BaseService use business
    """

    def __init__(self, current_user=None, pagination_params=None, is_init_session=True, websocket=None):
        self.current_user = current_user
        self.pagination_params = pagination_params
        self.errors = []
        self.websocket = websocket

        self.session: Optional[Session] = None
        if is_init_session:
            logging.info("Started session")
            self.session = SessionLocal()

    def _close_session(self):
        if self.session:
            self.session.close()
            logging.info("Closed session")

    def call_repos(self, result_call_repos: ReposReturn):
        if result_call_repos.is_error:
            self.response_exception(
                msg=result_call_repos.msg,
                loc=result_call_repos.loc,
                detail=result_call_repos.detail
            )

        return result_call_repos.data

    def append_error(self, msg: str, loc: str = "", detail: str = ""):
        self.errors.append(Error(msg=msg, detail=detail, loc=loc))

    def _raise_exception(self, error_status_code=status.HTTP_400_BAD_REQUEST):
        errors = []
        for temp in self.errors:
            errors.append(temp.dict())
        raise ExceptionHandle(errors=errors, status_code=error_status_code)

    def response_exception(self, msg, loc="", detail="", error_status_code=status.HTTP_400_BAD_REQUEST):
        self._close_session()

        self.append_error(msg=msg, loc=loc, detail=detail)
        self._raise_exception(error_status_code=error_status_code)

    def response(self, data, error_status_code=status.HTTP_400_BAD_REQUEST):
        self._close_session()

        if self.errors:
            self._raise_exception(error_status_code=error_status_code)
        else:
            return {
                "data": data,
                "errors": self.errors,
            }
