from django.urls import path
from . import views

app_name = 'hutao'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('commands/', views.commands, name = 'commands'),
    path('notfound/', views.notfound, name = 'notfound'),
]