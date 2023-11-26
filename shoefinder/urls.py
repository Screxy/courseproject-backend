from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views
from .views import BrandViewSet, PurchaseLinksViewSet, ShoeModelsViewSet

app_name = 'shoefinder'

router = DefaultRouter()
router.register("brand", BrandViewSet)
router.register("model", ShoeModelsViewSet)
router.register("link", PurchaseLinksViewSet)

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:question_id>/", views.detail, name="detail"),
    path("polls", views.polls, name="polls"),
    path("find", views.find, name="find"),
]

urlpatterns.extend(router.urls)
