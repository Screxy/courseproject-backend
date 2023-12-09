from django.http import Http404
from django.shortcuts import render
from django_filters import filters
from django_filters.rest_framework import FilterSet, DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import ShoeModels, PurchaseLinks, Brand, Colors, Styles
from .pagination import ShoeModelPagination, PurchaseLinksPagination
from .serializers import BrandSerializer, ShoeModelsSerializer, PurchaseLinksSerializer
from .utils import filter_shoe_models


def index(request):
    models_name = ShoeModels.objects.all()
    context = {"models_name": models_name}
    return render(request, "shoefinder/list.html", context)


def detail(request, question_id):
    try:
        model_name = ShoeModels.objects.get(pk=question_id)
        links = PurchaseLinks.objects.filter(model=model_name)
    except ShoeModels.DoesNotExist:
        raise Http404("ShoeModels does not exist")
    return render(request, "shoefinder/detail.html", {"model_name": model_name, 'links': links})


def polls(request):
    try:
        brands = Brand.objects.all()
        styles = Styles.objects.all()
        colors = Colors.objects.all()
        context = {'brands': brands, 'styles': styles, 'colors': colors}
    except:
        raise Http404("Ошибка")
    return render(request, "shoefinder/polls.html", context)


def find(request):
    selected_brands = request.POST.getlist('choiceBrands')
    selected_colors = request.POST.getlist('choiceColors')
    selected_styles = request.POST.getlist('choiceStyles')

    shoe_models = filter_shoe_models(selected_brands, selected_colors, selected_styles)

    context = {
        'brands': selected_brands,
        'styles': selected_styles,
        'colors': selected_colors,
        'models': shoe_models
    }

    return render(request, "shoefinder/findedShoes.html", context)


class BrandViewSet(ModelViewSet):
    serializer_class = BrandSerializer
    queryset = Brand.objects.all()


class ShoeModelsFilter(FilterSet):
    class Meta:
        model = ShoeModels
        fields = ['brand']


class ShoeModelsViewSet(ModelViewSet):
    serializer_class = ShoeModelsSerializer
    queryset = ShoeModels.objects.all()
    pagination_class = ShoeModelPagination
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = ShoeModelsFilter
    search_fields = ['name', 'brand__name', 'color__name']

    def get_queryset(self):
        brand_name = self.request.query_params.get('brand', None)
        if brand_name:
            return ShoeModels.objects.filter(brand__name__icontains=brand_name)
        return ShoeModels.objects.all()

    @action(detail=True, methods=['POST'])
    def add_purchase_link(self, request, pk=None):
        shoe_model = self.get_object()
        data = request.data
        data['model'] = shoe_model.id

        serializer = PurchaseLinksSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)


class PurchaseLinksViewSet(ModelViewSet):
    serializer_class = PurchaseLinksSerializer
    queryset = PurchaseLinks.objects.all()
    pagination_class = PurchaseLinksPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['store_name']

    @action(detail=False, methods=['GET'])
    def average_price_by_brand(self, request):
        brand_name = request.query_params.get('brand', None)

        if brand_name:
            shoes = ShoeModels.objects.filter(brand__name=brand_name)
            total_price = sum(link.price for link in PurchaseLinks.objects.filter(model__in=shoes))
            average_price = total_price / len(shoes) if len(shoes) > 0 else 0
            return Response({'average_price': average_price})
        else:
            return Response({'error': 'Provide a brand parameter'})

    @action(detail=False, methods=['GET'])
    def search_by_color_and_style(self, request):
        color_name = request.query_params.get('color', None)
        style_name = request.query_params.get('style', None)

        if color_name and style_name:
            shoes = ShoeModels.objects.filter(color__name=color_name, style__name=style_name)
            serializer = ShoeModelsSerializer(shoes, many=True)
            return Response(serializer.data)
        else:
            return Response({'error': 'Provide both color and style parameters'})


class FindModelsViewSet(viewsets.ViewSet):
    serializer_class = ShoeModelsSerializer

    def create(self, request):
        selected_brands = request.data.get('choiceBrands', [])
        selected_colors = request.data.get('choiceColors', [])
        selected_styles = request.data.get('choiceStyles', [])

        shoe_models = filter_shoe_models(selected_brands, selected_colors, selected_styles)

        serializer = self.serializer_class(shoe_models, many=True)

        response_data = {
            'brands': selected_brands,
            'styles': selected_styles,
            'colors': selected_colors,
            'models': serializer.data
        }

        return Response(response_data)
