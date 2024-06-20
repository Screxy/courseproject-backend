from django.contrib.auth.models import User
from django.db import models


class VkUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    vk_user_id = models.IntegerField()
    access_token = models.TextField()
