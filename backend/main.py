import os

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers import messages, groups, manage, users
from utils.db import init_models


app = FastAPI(title='TelegramUserBot')
app.include_router(users.router, tags=['Endpoints for site'])
app.include_router(manage.router, tags=['Manage'])
app.include_router(messages.router, tags=['Messages'])
app.include_router(groups.router, tags=['Groups'])

origins = ["http://localhost:8080", "https://frontend-vue-production.up.railway.app"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event('startup')
async def startup():
    await init_models()


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv('PORT')))



