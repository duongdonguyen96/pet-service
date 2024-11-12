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