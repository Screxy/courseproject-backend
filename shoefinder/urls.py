from django.urls import path

from . import views

app_name = 'shoefinder'

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:question_id>/", views.detail, name="detail"),
    path("polls", views.polls, name="polls"),
    path("find", views.find, name="find"),
]
