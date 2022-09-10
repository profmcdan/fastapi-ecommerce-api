from pydantic import BaseModel
from tortoise.contrib.pydantic import pydantic_model_creator
from .models import Product


ProductSerializer = pydantic_model_creator(Product, name='Product')
CreateProductSerializer = pydantic_model_creator(Product, name='ProductIn', exclude_readonly=True,
                                                 exclude=('percentage_discount',))
