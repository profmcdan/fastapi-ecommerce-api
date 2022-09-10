from pydantic import BaseModel
from tortoise.contrib.pydantic import pydantic_model_creator
from .models import User


UserSerializer = pydantic_model_creator(User, name='User', exclude=('verified', 'password'))
CreateUserSerializer = pydantic_model_creator(User, name='UserIn', exclude_readonly=True, exclude=('verified',))
