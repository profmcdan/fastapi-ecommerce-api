import uuid
from datetime import datetime
from tortoise import Model, fields
from pydantic import BaseModel


class Business(Model):
    id = fields.UUIDField(pk=True, default=uuid.uuid4, index=True)
    name = fields.CharField(max_length=256, unique=True)
    city = fields.CharField(max_length=100)
    region = fields.CharField(max_length=100)
    description = fields.TextField(null=True)
    logo = fields.CharField(max_length=256, null=True)
    admin = fields.ForeignKeyField('models.User', related_name='business')
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    def __str__(self):
        return self.name
