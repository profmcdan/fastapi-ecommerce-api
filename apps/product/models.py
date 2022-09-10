import uuid
from datetime import datetime
from tortoise import Model, fields
from pydantic import BaseModel


class Product(Model):
    id = fields.UUIDField(pk=True, default=uuid.uuid4, index=True)
    business = fields.ForeignKeyField('models.Business', related_name='products')
    name = fields.CharField(max_length=200, index=True)
    category = fields.CharField(max_length=200)
    original_price = fields.DecimalField(max_digits=12, decimal_places=2)
    new_price = fields.DecimalField(max_digits=12, decimal_places=2)
    percentage_discount = fields.IntField(default=0)
    offer_expiration = fields.DateField(default=datetime.utcnow)
    image = fields.CharField(max_length=256, null=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    def __str__(self):
        return self.name
