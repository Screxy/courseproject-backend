from django.db.models import Q
from .models import ShoeModels

def find_matching_shoes(selected_brands, selected_colors, selected_styles):
    query = Q()

    for brand in selected_brands:
        query |= Q(brand__name=brand)

    for color in selected_colors:
        query &= Q(shoecolors__color__name=color)

    for style in selected_styles:
        query &= Q(shoestyles__style__name=style)

    matching_shoes = ShoeModels.objects.filter(query).distinct()

    return matching_shoes