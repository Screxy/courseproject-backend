from .models import Brand, ShoeModels, PurchaseLinks, Colors, Styles
from rest_framework import serializers


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Colors
        fields = '__all__'


class StyleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Styles
        fields = '__all__'


class ShoeModelsSerializer(serializers.ModelSerializer):
    brand = BrandSerializer()
    color = ColorSerializer(many=True)
    style = StyleSerializer(many=True)

    class Meta:
        model = ShoeModels
        fields = ('id', 'name', 'brand', 'color', 'style')


class PurchaseLinksSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseLinks
        fields = '__all__'
