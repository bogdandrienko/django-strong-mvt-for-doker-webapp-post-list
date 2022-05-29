from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.utils import timezone
from . import models

# Create your views here.


def index(request):
    return HttpResponse("<h1>This is a Index Page</h1>")


def home(request):
    context = {
    }
    return render(request, 'pages/home.html', context)


def create(request):
    if request.method == 'POST':
        title = request.POST.get("title", "")
        description = request.POST.get("description", "")
        models.Post.objects.create(
            title=title,
            description=description,
            is_completed=False,
        )
        return redirect(reverse('app_name_post_list:create', args=()))
        # return redirect(reverse('app_name_post_list:read_list', args=()))
    categories = [
        {"name": "Новое", "value": "new"},
        {"name": "Старое", "value": "old"},
        {"name": "Опубликованное", "value": "public"},
        {"name": "Приватное", "value": "private"},
    ]
    context = {
        "categories": categories,
    }
    return render(request, 'app_post_list/pages/post_create.html', context)
