from sqlalchemy import VARCHAR, Column, ForeignKey, Boolean
from sqlalchemy.orm import relationship

from app.third_parties.db.base import CustomBaseModel, Base


class User(Base, CustomBaseModel):
    __tablename__ = 'users'

    first_name = Column(VARCHAR(105), nullable=False, comment='Tên')
    last_name = Column(VARCHAR(105), nullable=False, comment='Họ')
    email = Column(VARCHAR(100), comment='Email')
    phone = Column(VARCHAR(12), comment='Số điện thoại')
    username = Column('username', VARCHAR(50), comment='tên tài khoản', unique=True, index=True)
    gender = Column(Boolean(), default=1)
    password = Column(VARCHAR(100), nullable=False)
    is_admin = Column(Boolean(), default=0)

    roles = relationship("Role", secondary="user_roles")


class Role(Base, CustomBaseModel):
    __tablename__ = 'roles'

    name = Column(VARCHAR(50), unique=True, index=True)

    permissions = relationship("Permission", secondary="role_permissions")


class Permission(Base, CustomBaseModel):
    __tablename__ = 'permissions'

    name = Column(VARCHAR(50), unique=True, index=True)


class RolePermission(Base, CustomBaseModel):
    __tablename__ = 'role_permissions'
    role_id = Column(VARCHAR(32), ForeignKey('roles.id', ondelete="CASCADE"))
    permission_id = Column(VARCHAR(32), ForeignKey('permissions.id', ondelete="CASCADE"))


class UserRole(Base, CustomBaseModel):
    __tablename__ = 'user_roles'
    user_id = Column(VARCHAR(32), ForeignKey('users.id', ondelete="CASCADE"))
    role_id = Column(VARCHAR(32), ForeignKey('roles.id', ondelete="CASCADE"))
