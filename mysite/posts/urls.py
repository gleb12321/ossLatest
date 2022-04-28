from django.urls import path
from . import views

app_name = "posts"
urlpatterns = [
    path('', views.index, name='index'),
    path('group_list', views.group_list, name='group_list'),
    path('windows10', views.about, name='about'),
    path('register', views.register, name='register')
]
