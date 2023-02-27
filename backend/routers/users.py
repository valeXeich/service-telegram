from typing import List

from fastapi import APIRouter, Depends, status, HTTPException

from auth.auth import current_user
from db.db import get_session
from services import users
from schemas.users import UserLogin, Account, UserBot, AccountUpdate
from schemas.general import SuccessResponse
from utils.secrets import create_secret_key

router = APIRouter()


@router.get('/get-instances', response_model=List[Account], status_code=status.HTTP_200_OK, summary='Получение аккаунтов')
async def get_instances(session = Depends(get_session), user = Depends(current_user)):
    instances = await users.get_accounts(user['user'].tg_id, session)
    return instances


@router.get('/get-instance', response_model=Account, status_code=status.HTTP_200_OK, summary='Получить аккаунт')
async def get_instance(id: int, session = Depends(get_session), user = Depends(current_user)):
    account = await users.get_account_by_user(id, user['user'], session)
    if account:
        return account
    raise HTTPException(status.HTTP_404_NOT_FOUND, 'Not found')


@router.get('/get-bot-data', response_model=UserBot, status_code=status.HTTP_200_OK, summary='Получить api_id/app_hash')
async def get_bot_data(user = Depends(current_user)):
    data = {'bot_id': user['user'].bot_id, 'bot_hash': user['user'].bot_hash}
    return data


@router.post('/login', status_code=status.HTTP_201_CREATED, summary='Логин в кабинет')
async def login(request: UserLogin, session = Depends(get_session)):
    user = await users.get_user(request.tg_id, session)
    if not user:
        await users.create_user(request.tg_id, request.username, session)
    data = {'tg_id': request.tg_id, 'username': request.username}
    token = create_secret_key(data, 'HS256')
    return {'token': token}


@router.post('/create-instance', status_code=status.HTTP_201_CREATED, response_model=Account, summary='Создать аккаунт')
async def create_instance(session = Depends(get_session), user = Depends(current_user)):
    account = await users.create_account(user['user'].tg_id, user['user'], session)
    return account


@router.post('/change-bot-data', status_code=status.HTTP_201_CREATED, response_model=SuccessResponse, summary='Обновить данные api_id/app_hash')
async def change_bot_data(request: UserBot, session = Depends(get_session), user = Depends(current_user)):
    await users.change_bot_data(request.bot_id, request.bot_hash, user['user'], session)
    return {'ok': True}


@router.patch('/update-instance', status_code=status.HTTP_200_OK, response_model=SuccessResponse, summary='Обновить настройки аккаунта')
async def update_instance(account_id: int, request: AccountUpdate, session = Depends(get_session), user = Depends(current_user)):
    await users.update_account(account_id, request, session)
    return {'ok': True}