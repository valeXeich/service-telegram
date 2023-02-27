import json

from fastapi import APIRouter, Depends, status, HTTPException
from pyrogram.errors import RPCError
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from auth.auth import current_user
from schemas.general import SuccessResponse
from utils.client import get_client
from utils.tasks import distribution

router = APIRouter()


@router.get('/telegram/get-contacts', status_code=status.HTTP_200_OK, summary='Получить контакты (keyword = first_name)')
async def get_contacts(keyword: str = None, user = Depends(current_user)):
    try:
        client = await get_client(user['user'], account=user['account'])
        counter = 0
        result = []
        contacts = await client.get_contacts()
        contacts = json.loads(str(contacts))
        if keyword:
            for contact in contacts:
                if keyword.lower() in contact['first_name'].lower():
                    result.append(contact)
                    counter += 1
                if counter == 10800:
                    break
            return result
        return contacts
    except RPCError as e:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, str(e))


@router.post('/telegram/send-message', response_model=SuccessResponse, status_code=status.HTTP_200_OK, summary='Отправить сообщение')
async def send_message(chat_id: str, message: str, user = Depends(current_user)):
    try:
        client = await get_client(user['user'], account=user['account'])
        await client.send_message(chat_id, message)
        return {'ok': True}
    except RPCError as e:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, str(e))


@router.post('/telegram/send-location', response_model=SuccessResponse, status_code=status.HTTP_200_OK, summary='Отправить локацию')
async def send_location(chat_id: str, latitude: float, longitude: float, user = Depends(current_user)):
    try:
        client = await get_client(user['user'], account=user['account'])
        await client.send_location(chat_id, latitude, longitude)
        return {'ok': True}
    except RPCError as e:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, str(e))


@router.post('/telegram/send-photo', response_model=SuccessResponse, status_code=status.HTTP_200_OK, summary='Отправить фото')
async def send_photo(chat_id: str, photo_url: str, caption: str = 'caption', user = Depends(current_user)):
    try:
        client = await get_client(user['user'], account=user['account'])
        await client.send_photo(chat_id, photo_url, caption)
        return {'ok': True}
    except RPCError as e:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, str(e))


@router.post('/telegram/send-video', response_model=SuccessResponse, status_code=status.HTTP_200_OK, summary='Отправить видео')
async def send_video(chat_id: str, video_url: str, caption: str = 'caption', file_name: str = 'file_name', user = Depends(current_user)):
    try:
        client = await get_client(user['user'], account=user['account'])
        await client.send_video(chat_id, video_url, caption, file_name=file_name)
        return {'ok': True}
    except RPCError as e:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, str(e))


@router.post('/telegram/send-voice', response_model=SuccessResponse, status_code=status.HTTP_200_OK, summary='Отправить аудио')
async def send_voice(chat_id: str, voice_url: str, caption: str = 'caption', user = Depends(current_user)):
    try:
        client = await get_client(user['user'], account=user['account'])
        await client.send_voice(chat_id, voice_url, caption)
        return {'ok': True}
    except RPCError as e:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, str(e))


@router.post('/telegram/send-cached-media', response_model=SuccessResponse, status_code=status.HTTP_200_OK, summary='Отправить файл с кэша')
async def send_cached_media(chat_id: str, file_id: str, caption: str = 'caption', user = Depends(current_user)):
    try:
        client = await get_client(user['user'], account=user['account'])
        await client.send_cached_media(chat_id, file_id, caption)
        return {'ok': True}
    except RPCError as e:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, str(e))


@router.post('/telegram/send-contact', response_model=SuccessResponse, status_code=status.HTTP_200_OK, summary='Отправить контакт')
async def send_contact(chat_id: str, phone_number: str, first_name: str, last_name: str, user = Depends(current_user)):
    try:
        client = await get_client(user['user'], account=user['account'])
        await client.send_contact(chat_id, phone_number, first_name, last_name)
        return {'ok': True}
    except RPCError as e:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, str(e))


@router.post('/telegram/mass/send-message', status_code=status.HTTP_200_OK, summary='Рассылка по контактам телеграм аккаунта (каждые 30 сек)')
async def send_mass_message(user = Depends(current_user)):
    try:
        client = await get_client(user['user'], account=user['account'])
        scheduler = AsyncIOScheduler()
        scheduler.add_job(distribution, "interval", seconds=30, args=[client])
        scheduler.start()
        return {'ok': True}
    except RPCError as e:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, str(e))


