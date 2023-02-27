from fastapi import Depends, HTTPException, Security, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from jose import JWTError

from utils.secrets import decode_secret_key
from db.db import get_session
from services.users import get_user, get_account

token = HTTPBearer()


async def current_user(
    token_header: HTTPAuthorizationCredentials = Security(token),
    session = Depends(get_session)
):
    try:
        data = decode_secret_key(token_header.credentials, 'HS256')
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Could not validate token"
        )
    user = await get_user(data.get('tg_id'), session)
    user_info = {'user': user}
    account_id = data.get('account_id')
    if account_id:
        account = await get_account(account_id, session)
        user_info['account'] = account
    if user:
        return user_info
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Could not validate token"
        )