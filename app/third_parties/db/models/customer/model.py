from sqlalchemy import VARCHAR, Column, ForeignKey
from sqlalchemy.orm import relationship

from app.third_parties.db.base import CustomBaseModel, Base
from app.third_parties.db.models.company.model import Company


class Customer(Base, CustomBaseModel):
    __tablename__ = 'customer'

    full_name = Column(VARCHAR(105), nullable=False, comment='Tên đầy đủ')
    email = Column(VARCHAR(100), comment='Email')
    phone = Column(VARCHAR(12), comment='Số điện thoại')
    username = Column('username', VARCHAR(50), comment='tên tài khoản', unique=True)
    gender = Column(VARCHAR(10))

    company_id = Column(ForeignKey('company.id'), nullable=True)
    company = relationship('Company')
