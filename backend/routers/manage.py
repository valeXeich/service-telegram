from fastapi import APIRouter, Depends, HTTPException, status
from pyrogram.errors import RPCError

from utils.client import get_client
from schemas.general import SuccessResponse, PhoneHashCode
from auth.auth import current_user

router = APIRouter()


@router.post('/telegram/login', response_model=SuccessResponse, status_code=status.HTTP_200_OK, summary='Логин в телеграм (выполнять после отправки кода)')
async def login_telegram(phone_number: str, phone_code: str, phone_code_hash: str, user = Depends(current_user)):
    client = await get_client(user['user'], True, user.get('account'))
    try:
        await client.connect()
    except ConnectionError:
         pass
    try:
        await client.sign_in(phone_number=phone_number, phone_code=phone_code, phone_code_hash=phone_code_hash)
    except RPCError as e:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, str(e))
    await client.disconnect()
    return {"ok": True}


@router.post('/telegram/send-code', response_model=PhoneHashCode, status_code=status.HTTP_200_OK, summary='Отправить код для логина (в ответе phone_code_hash)')
async def send_code(phone_number: str, user = Depends(current_user)):
    client = await get_client(user['user'], True, user.get('account'))
    try:
        await client.connect()
    except ConnectionError:
         pass
    try:
        result = await client.send_code(phone_number)
    except RPCError as e:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, str(e))
    return {'phone_code_hash': result.phone_code_hash}