from typing import Any, List
from typing import Generic, TypeVar

from pydantic import BaseModel
from pydantic import Field

TypeX = TypeVar("TypeX")


class Error(BaseModel):
    loc: str = Field(..., description='location')
    msg: str = Field(..., description='message')
    detail: str = Field(..., description='detail')


class ResponseData(BaseModel, Generic[TypeX]):
    data: TypeX = Field(..., description='data response with success status code')
    errors: List[Error] = []


class ResponseError(BaseModel):
    data: Any = None
    errors: List[Error] = Field(..., description='error response with fail status code')


class UserInfo(BaseModel):
    user_id: str = Field(..., description='user_id', example='103C76ECBBC144B7B589C6808C029016')
    username: str = Field(..., description='Tên tài khoản', example='ddonguyen')
    first_name: str = Field(..., description='Tên', example='Đỗ Nguyên')
    last_name: str = Field(..., description='Họ', example='Dương')
    email: str = Field(..., description='Thư điện tử', example='ddonguyen@cmc.com.vn')
    is_admin: bool = Field(..., description='is_admin', example=True)
    token_type: str = Field(..., description='Loại token')


class Authentication(BaseModel):
    username: str = Field(..., description='Tài khoản', example='ddonguyen')
    password: str = Field(..., description='Mật khẩu', example='123456')


class AuthenticationRes(BaseModel):
    access_token: str = Field(..., description='access_token', example='103C76ECBBC144B7B589C6808C029016')
    refresh_token: str
    expire: int
