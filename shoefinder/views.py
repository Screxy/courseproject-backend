from django.shortcuts import render
from django.db.models import Q
from .models import ShoeModels, PurchaseLinks, Brand, Colors, Styles


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
        brands = Brand.objects.all();
        styles = Styles.objects.all();
        colors = Colors.objects.all();
        context = {'brands': brands, 'styles': styles, 'colors': colors}
    except:
        raise Http404("Ошибка")
    return render(request, "shoefinder/polls.html", context)


def find(request):
    selected_brands = request.POST.getlist('choiceBrands')
    selected_colors = request.POST.getlist('choiceColors')
    selected_styles = request.POST.getlist('choiceStyles')

    query = Q()

    for brand in selected_brands:
        query |= Q(brand__name=brand)

    for color in selected_colors:
        query &= Q(shoecolors__color__name=color)

    for style in selected_styles:
        query &= Q(shoestyles__style__name=style)

    shoe_models = ShoeModels.objects.filter(query).distinct()

    context = {
        'brands': selected_brands,
        'styles': selected_styles,
        'colors': selected_colors,
        'models': shoe_models
    }

    return render(request, "shoefinder/findedShoes.html", context)
#
