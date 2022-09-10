from typing import List, Optional, Type
from tortoise.signals import post_save
from tortoise import BaseDBAsyncClient

from business.serializers import BusinessSerializer
from .models import User
from business.models import Business


@post_save(User)
async def create_business(
        sender: "Type[User]",
        instance: User,
        created: bool,
        using_db: "Optional[BaseDBAsyncClient]",
        update_fields: List[str]) -> None:
    if created:
        business_obj = await Business.create(name=instance.username, owner=instance)
        await BusinessSerializer.from_tortoise_orm(business_obj)
        # TODO: Send the email
