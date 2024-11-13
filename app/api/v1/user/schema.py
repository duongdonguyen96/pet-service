from pydantic import Field, BaseModel


class UserRq(BaseModel):
    first_name: str = Field(..., description='first_name')
    last_name: str = Field(..., description='last_name')
    email: str = Field(..., description='email')
    phone: str = Field(..., description='phone')
    gender: bool = Field(..., description='gender')
    username: str = Field(..., description='username')
    password: str = Field(...)


class UserRes(BaseModel):
    id: str = Field(..., description='id')
    username: str = Field(..., description='username')
    first_name: str = Field(..., description='first_name')
    last_name: str = Field(..., description='last_name')
    email: str = Field(..., description='email')
    phone: str = Field(..., description='phone')
    is_admin: bool = Field(...)
