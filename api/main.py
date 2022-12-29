import os

import uvicorn
from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware


DATABASE_URL = f'postgresql://{os.environ["DB_USER"]}:{os.environ["DB_PASSWORD"]}@{os.environ["DB_HOST"]}' \
               f'/{os.environ["DB_NAME"]}'

app = FastAPI()
app.add_middleware(DBSessionMiddleware, db_url=DATABASE_URL)


@app.get('/api/')
async def root():
    return {'message': 'hello world'}


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
