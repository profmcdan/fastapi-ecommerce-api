from fastapi import APIRouter
from .serializers import CreateUserSerializer, UserSerializer
from .models import User
from .authentication import hash_password

user_router = APIRouter()


@user_router.get('/', description='Users route')
async def index():
    return {'success': True, 'message': 'Welcome to users'}


@user_router.post('/registration', status_code=201)
async def register_user(user: CreateUserSerializer):
    user_info = user.dict(exclude_unset=True)
    user_info['password'] = hash_password(user_info.get('password'))
    user_obj = await User.create(**user_info)
    new_user = await UserSerializer.from_tortoise_orm(user_obj)
    return {'success': True, 'data': new_user}

