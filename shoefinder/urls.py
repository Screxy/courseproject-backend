from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views
from .views import BrandViewSet, PurchaseLinksViewSet, ShoeModelsViewSet, FindModelsViewSet

app_name = 'shoefinder'

router = DefaultRouter()
router.register("brands", BrandViewSet)
router.register("models", ShoeModelsViewSet)
router.register("links", PurchaseLinksViewSet)
router.register('find-models', FindModelsViewSet, basename='find-models')

urlpatterns = [
                  # path("", views.index, name="index"),
                  # path("<int:question_id>/", views.detail, name="detail"),
                  # path("polls", views.polls, name="polls"),
                  # path("find", views.find, name="find"),
              ] + router.urls
