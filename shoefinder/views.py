from django.shortcuts import render

from .models import ShoeModels


def index(request):
    models_name = ShoeModels.objects.all()
    context = {"models_name": models_name}
    return render(request, "shoefinder/list.html", context)


def detail(request, question_id):
    try:
        model_name = ShoeModels.objects.get(pk=question_id)
    except ShoeModels.DoesNotExist:
        raise Http404("ShoeModels does not exist")
    return render(request, "shoefinder/detail.html", {"model_name": model_name})
