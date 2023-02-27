from pydantic import BaseModel

from typing import List, Union


class Group(BaseModel):
    title: str
    users: List[Union[int, str]]


class GroupAddMebmer(BaseModel):
    chat_id: str
    users: List[Union[int, str]]


class GroupDelMember(BaseModel):
    chat_id: int
    user_id: int