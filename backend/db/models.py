from sqlalchemy import Column, Integer, String, ForeignKey, Boolean

from .db import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    tg_id = Column(Integer, nullable=False, unique=True)
    bot_id = Column(String, nullable=True)
    bot_hash = Column(String, nullable=True)


class Account(Base):
    __tablename__ = 'accounts'

    id = Column(Integer, primary_key=True, autoincrement=True)
    account_name = Column(String, nullable=True)
    proxy = Column(Boolean, default=False)
    proxy_ip = Column(String, nullable=True)
    proxy_port = Column(String, nullable=True)
    proxy_username = Column(String, nullable=True)
    proxy_password = Column(String, nullable=True)
    secret_key = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))



