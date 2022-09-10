from pydantic import BaseModel
from tortoise.contrib.pydantic import pydantic_model_creator
from .models import Business


BusinessSerializer = pydantic_model_creator(Business, name='Business')
CreateBusinessSerializer = pydantic_model_creator(Business, name='BusinessIn', exclude_readonly=True)
