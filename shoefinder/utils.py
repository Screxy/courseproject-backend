from functools import reduce
from django.db.models import Q

from shoefinder.models import ShoeModels


def filter_shoe_models(brands, styles, colors):
    """
    Функция для фильтрации моделей кроссовок по брендам, стилям и цветам.

    :param brands: Список брендов
    :param styles: Список стилей
    :param colors: Список цветов
    :return: QuerySet моделей кроссовок
    """
    # Используем Q-объекты для построения сложных запросов
    brand_q = Q(brand__name__in=brands) if brands else Q()
    style_q = Q(style__name__in=styles) if styles else Q()
    color_q = Q(color__name__in=colors) if colors else Q()

    # Выполняем запрос к базе данных
    shoe_models = ShoeModels.objects.filter(brand_q & style_q & color_q)

    return shoe_models
