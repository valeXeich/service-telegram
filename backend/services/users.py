from sqlalchemy import select, update
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException, status

from db.models import User, Account
from utils.secrets import create_secret_key


async def create_user(tg_id, tg_username, session):
    user = User(tg_id=tg_id, username=tg_username)
    session.add(user)
    await session.commit()


async def get_user(tg_id, session):
    query = select(User).where(User.tg_id == tg_id)
    result = await session.execute(query)
    return result.scalars().first()


async def create_account(tg_id, user, session):
    account = Account(secret_key='t', user_id=user.id)
    session.add(account)
    await session.flush()
    data = {'account_id': account.id, 'tg_id': tg_id}
    secret_key = create_secret_key(data, 'HS256')
    account.secret_key = secret_key
    await session.commit()
    return account


async def get_accounts(tg_id, session):
    query = select(Account).join(User, User.id == Account.user_id).where(User.tg_id == tg_id)
    result = await session.execute(query)
    return result.scalars().all()


async def change_bot_data(bot_id, bot_hash, user, session):
    query = update(User).where(User.id == user.id).values(bot_id=bot_id, bot_hash=bot_hash)
    await session.execute(query)
    await session.commit()


async def get_account(account_id, session):
    query = select(Account).where(Account.id == account_id)
    result = await session.execute(query)
    return result.scalars().first()


async def get_account_by_user(account_id, user, session):
    query = select(Account).where(Account.user_id == user.id and Account.id == account_id)
    result = await session.execute(query)
    return result.scalars().first()


async def update_account(account_id, data, session):
    query = update(Account).where(Account.id == account_id).values(**dict(data))
    await session.execute(query)
    await session.commit()