from django.urls import path, re_path
from . import views


app_name = 'app_name_post_list'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('', views.home, name=''),
    path('home/', views.home, name='home'),

    path('post/create/', views.create, name='create'),
    # path('task/<int:task_id>/', views.read, name='read'),
    # path('task/list/', views.read_list, name='read_list'),
    # path('task/<int:task_id>/update/', views.update, name='update'),
    # re_path(r'^task/(?P<task_id>\d+)/delete/$', views.delete, name='delete'),
]
