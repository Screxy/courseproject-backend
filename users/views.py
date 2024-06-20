import os

from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect
from rest_framework import status
from rest_framework.generics import (
    ListCreateAPIView,
)
from rest_framework.response import Response
from rest_framework.utils import json
from rest_framework_simplejwt.tokens import RefreshToken
import requests
from .task import send_email

from users.models import VkUser
from users.serializers import UserSerializer

User = get_user_model()


class RegistrationView(ListCreateAPIView):
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)

        return Response({'access_token': access_token}, status=status.HTTP_201_CREATED)


class Oauth(ListCreateAPIView):
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        data = json.loads(request.query_params['payload'])
        token = data['token']
        uuid = data['uuid']
        url = "https://api.vk.com/method/auth.exchangeSilentAuthToken"
        data = {
            "v": "5.131",
            "token": token,
            "access_token": os.getenv("SERVICE_TOKEN"),
            "uuid": uuid
        }
        response = requests.post(url, data=data)
        response_date = response.json()
        email = response_date['response']['email']
        try:
            user = User.objects.get(email=email)
            vk_access_token = response_date['response']['access_token']
            user.vkuser.access_token = vk_access_token
            user.save()
        except User.DoesNotExist:
            vk_access_token = response_date['response']['access_token']
            user_id = response_date['response']['user_id']
            url_users = 'https://api.vk.com/method/users.get'
            data_users = {
                "v": "5.199",
                "access_token": vk_access_token,
            }
            response = requests.post(url_users, data=data_users)
            response_json = response.json()['response'][0]
            first_name = response_json['first_name']
            last_name = response_json['last_name']
            user_data = {
                "first_name": first_name,
                "last_name": last_name,
                "email": email,
                "username": first_name,
                "password": '123456'
            }
            serializer = self.get_serializer(data=user_data)
            serializer.is_valid(raise_exception=True)
            user = serializer.save()
            VkUser.objects.create(user=user, vk_user_id=user_id, access_token=vk_access_token)

        send_email.delay(user.pk)
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)
        refresh_token = str(refresh),
        return HttpResponseRedirect('http://localhost:5173/oauth?access_token='
                                    + access_token + '&refresh_token=' + refresh_token[0])
