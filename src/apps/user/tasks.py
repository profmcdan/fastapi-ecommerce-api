from typing import List
from celery import shared_task
from .models import User


@shared_task(bind=True, autoretry_for=(Exception,), retry_backoff=True, retry_kwargs={'max_retries': 5},
             name='users:send_email')
def send_new_user_email(self, data: object):
    print(data)
