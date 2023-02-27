import os

from jose import jwt

SECRET_KEY = os.getenv('SECRET_KEY')


def create_secret_key(data: dict, ALGORITHM):
    to_encode = data.copy()
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def decode_secret_key(token, ALGORITHM):
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    return payload
