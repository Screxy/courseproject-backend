from .models import Brand, ShoeModels, PurchaseLinks
from rest_framework import serializers


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'


class ShoeModelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoeModels
        fields = '__all__'


class PurchaseLinksSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseLinks
        fields = '__all__'
