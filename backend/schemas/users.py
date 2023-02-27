from typing import Union, Optional

from pydantic import BaseModel


class UserBot(BaseModel):
    bot_id: Union[str, None]
    bot_hash: Union[str, None]


class UserLogin(BaseModel):
    tg_id: int
    username: str


class AccountUpdate(BaseModel):
    account_name: Optional[str] = None
    proxy: Optional[bool] = None
    proxy_ip: Optional[str] = None
    proxy_port: Optional[str] = None
    proxy_username: Optional[str] = None
    proxy_password: Optional[str] = None


class Account(BaseModel):
    id: int
    account_name: Union[str, None]
    secret_key: str
    user_id: int
    proxy: bool
    proxy_ip: Union[str, None]
    proxy_port: Union[str, None]
    proxy_username: Union[str, None]
    proxy_password: Union[str, None]

    class Config:
        orm_mode = True