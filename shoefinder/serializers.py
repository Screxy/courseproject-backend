from .models import Brand, ShoeModels, PurchaseLinks
from rest_framework import serializers


class BrandSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Brand
        fields = ['name']


class ShoeModelsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ShoeModels
        fields = ['brand', 'name']


class PurchaseLinksSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PurchaseLinks
        fields = ['model', 'store_name', 'url', 'price']
