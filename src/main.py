import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from tortoise.contrib.fastapi import register_tortoise
from configs.settings import get_settings
from apps.user.views import user_router

app = FastAPI()
app.include_router(user_router, prefix='/api/v1/users', tags=['users'])


register_tortoise(
    app,
    db_url=get_settings().DATABASE_URL,
    modules={'models': [
        'apps.user.models',
        'apps.business.models',
        'apps.product.models',
        'aerich.models'
    ]},
    generate_schemas=True,
    add_exception_handlers=True
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)


@app.get("/")
async def index():
    return {'message': "Hello World"}

if __name__ == '__main__':
    uvicorn.run("main:app", host='127.0.0.1', port=8000, reload=True)
