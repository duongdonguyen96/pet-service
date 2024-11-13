from sqlalchemy import Column, String, VARCHAR, ForeignKey
from sqlalchemy.orm import relationship

from app.third_parties.db.base import CustomBaseModel, Base


class LoginHistory(Base, CustomBaseModel):
    __tablename__ = 'login_history'

    user_id = Column(VARCHAR(32), ForeignKey('users.id'), nullable=False)
    ip_address = Column(VARCHAR())
    device_info = Column(VARCHAR())
    status = Column(VARCHAR(20))
    location = Column(VARCHAR())
    access_token = Column(VARCHAR(), nullable=True)
    refresh_token = Column(VARCHAR(), nullable=True)
    jti = Column(VARCHAR(32), nullable=True, unique=True)

    user = relationship("User", back_populates="login_history")


class TokenBlacklist(Base, CustomBaseModel):
    __tablename__ = 'token_blacklist'

    jti = Column(VARCHAR(32), nullable=False, unique=True)
