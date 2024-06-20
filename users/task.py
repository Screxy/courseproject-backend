from celery import shared_task
from django.contrib.auth.models import User


@shared_task
def send_email(user_pk):
    user = User.objects.get(pk=user_pk)

