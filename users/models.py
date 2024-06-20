from django.contrib.auth.models import User
from django.db import models


class VkUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    vk_user_id = models.IntegerField()
    access_token = models.TextField()


class UserVisit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    url = models.TextField()
    os = models.TextField()
    browser = models.TextField()
    get_params = models.TextField(null=True, blank=True)
    post_params = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.user} visited {self.url} on {self.date}'

