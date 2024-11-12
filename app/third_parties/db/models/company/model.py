from sqlalchemy import VARCHAR, Column

from app.third_parties.db.base import CustomBaseModel, Base


class Company(Base, CustomBaseModel):
    __tablename__ = 'company'

    name = Column(VARCHAR(105), nullable=False, comment='Tên công ty')
    address = Column(VARCHAR(100), comment='Địa chỉ công ty')
    # phone = Column(VARCHAR(12), comment='Số điện thoại')
