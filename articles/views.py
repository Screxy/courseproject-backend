from django.http import Http404, HttpResponseRedirect

from django.shortcuts import render

from django.urls import reverse

from .models import Article, Comment

from django.core.files import File


def index(request):
    latest_articles_list = Article.objects.order_by('-pub_date')[:5]
    return render(request, 'articles/list.html', {'latest_articles_list': latest_articles_list})


def detail(request, article_id):
    try:
        a = Article.objects.get(id=article_id)


    except:
        raise Http404("Статья не найдена")

    latest_comments_list = a.comment_set.order_by('id')[:10]

    return render(request, 'articles/detail.html', {'article': a, 'latest_comments_list': latest_comments_list})


def leave_comment(request, article_id):
    try:
        a = Article.objects.get(id=article_id)

    except:
        raise Http404("Статья не найдена")

    comment = a.comment_set.create(author_name=request.POST['username'], comment_text=request.POST['comment'])
    if 'image' in request.FILES:
        comment.image = request.FILES['image']
        comment.save()

    return HttpResponseRedirect(reverse('articles:detail', args=(a.id,)))


def delete_comment(request, article_id, comment_id):
    try:
        article = Article.objects.get(id=article_id)
        comment = Comment.objects.get(id=comment_id)

    except:
        raise Http404("Комментарий не найден")

    comment.delete()

    return HttpResponseRedirect(reverse('articles:detail', args=(article.id,)))


def detail_comment(request, article_id, comment_id):
    try:
        comment = Comment.objects.get(id=comment_id)
        article = Article.objects.get(id=article_id)

    except:
        raise Http404("comment не найден")

    return render(request, 'articles/detail_comment.html', {'comment': comment, 'article': article})


def edit_comment(request, article_id, comment_id):
    try:
        article = Article.objects.get(id=article_id)
        comment = Comment.objects.get(id=comment_id)
    except:
        raise Http404("Комментарий к статье не найден")
    if 'image' in request.FILES:
        comment.image = request.FILES['image']
        print('asdasdasdasd')
        comment.save()
    comment.comment_text = request.POST['comment']
    comment.save()
    return HttpResponseRedirect(reverse('articles:detail_comment', args=(article.id, comment.id,)))
