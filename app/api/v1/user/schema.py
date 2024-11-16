from pydantic import Field, BaseModel, validator


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


class ChangePasswordRq(BaseModel):
    old_password: str = Field(..., description='old_password', min_length=6)
    new_password: str = Field(..., description='new_password', min_length=6)
    re_new_password: str = Field(..., description='re_new_password', min_length=6)

    @validator('re_new_password')
    def validate_re_new_password(cls, v, values):
        if 'new_password' in values and v != values['new_password']:
            raise ValueError('re_new_password is not match new_password!')
        if v == values['old_password']:
            raise ValueError('new password must be different from old password!')
        return v
