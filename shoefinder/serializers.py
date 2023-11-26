from .models import Brand, ShoeModels, PurchaseLinks
from rest_framework import serializers


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['name']


class ShoeModelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoeModels
        fields = ['brand', 'name']


class PurchaseLinksSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseLinks
        fields = ['model', 'store_name', 'url', 'price']
