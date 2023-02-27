from pyrogram import Client
from pyrogram.errors import RPCError
from fastapi import HTTPException, status


clients = {}

async def get_client(user, login=False, account=False):
    try:
        global clients
        proxy = {}
        if account:
            if account.proxy and account.proxy_ip and account.proxy_port:
                proxy = {
                    'scheme': 'socks5', 
                    'hostname': account.proxy_ip, 
                    'port': account.proxy_port
                }
                if account.proxy_username and account.proxy_password:
                    proxy['username'] = account.proxy_username
                    proxy['password'] = account.proxy_password
        if not user.bot_id or not user.bot_hash:
            raise HTTPException(status.HTTP_400_BAD_REQUEST, 'Не заполнено api_id/api_hash')
        client = clients.get(user.id)
        if client and not login:
            client.proxy = proxy
            try:
                await client.start()
            except ConnectionError:
                pass
            return client
        elif client and login:
            client.proxy = proxy
            return client
        elif not client and login:
            client = Client(
                'telegram_bot', 
                api_id=user.bot_id, 
                api_hash=user.bot_hash,
                proxy=proxy
            )
            clients[user.id] = client
            return client
        else:
            raise HTTPException(status.HTTP_400_BAD_REQUEST, 'Вы не авторизованы')
    except RPCError as e:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, str(e))
        
    
    