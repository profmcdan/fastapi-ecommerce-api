import uuid
from datetime import datetime
from tortoise import Model, fields


class User(Model):
    id = fields.UUIDField(pk=True, default=uuid.uuid4, index=True)
    username = fields.CharField(max_length=100, unique=True, null=False)
    firstname = fields.CharField(max_length=100)
    lastname = fields.CharField(max_length=100)
    email = fields.CharField(max_length=100, unique=True)
    password = fields.CharField(max_length=256)
    verified = fields.BooleanField(default=False)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    def __str__(self):
        return self.username
