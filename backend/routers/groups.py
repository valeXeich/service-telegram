from fastapi import APIRouter, Depends, status, HTTPException
from pyrogram.errors import RPCError

from auth.auth import current_user
from utils.client import get_client
from schemas import groups, general

router = APIRouter()


@router.post('/telegram/groups/create', response_model=general.SuccessResponse, status_code=status.HTTP_200_OK, summary='Создать группу')
async def group_create(request: groups.Group, user = Depends(current_user)):
    try:
        client = await get_client(user['user'], account=user.get('account'))
        await client.create_group(request.title, request.users)
        return {'ok': True}
    except RPCError as e:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, str(e))


@router.post('/telegram/groups/add-member', response_model=general.SuccessResponse, status_code=status.HTTP_200_OK, summary='Добавить в группу')
async def group_add_member(request: groups.GroupAddMebmer, user = Depends(current_user)):
    try:
        client = await get_client(user['user'], account=user.get('account'))
        await client.add_chat_members(request.chat_id, request.users)
        return {'ok': True}
    except RPCError as e:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, str(e))


@router.post('/telegram/groups/del-member', response_model=general.SuccessResponse, status_code=status.HTTP_200_OK, summary='Удалить из группы')
async def group_del_member(request: groups.GroupDelMember, user = Depends(current_user)):
    try:
        client = await get_client(user['user'], account=user.get('account'))
        await client.ban_chat_member(request.chat_id, request.user_id)
        return {'ok': True}
    except RPCError as e:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, str(e))
