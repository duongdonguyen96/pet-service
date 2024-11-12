from pydantic import Field, BaseModel


class CustomerRq(BaseModel):
    fullname: str = Field(..., description='fullname')
    email: str = Field(..., description='email')
    phone: str = Field(..., description='phone')
    gender: str = Field(..., description='gender')
    username: str = Field(..., description='username')


class CustomersRes(BaseModel):
    id: str = Field(..., description='id')
    username: str = Field(..., description='username')
    fullname: str = Field(..., description='fullname')
    email: str = Field(..., description='email')
    phone: str = Field(..., description='phone')
