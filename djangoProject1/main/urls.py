from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='main'),  # здесь мы переходим в функцию index в файле views
    path('about', views.about, name='about'),
    path('create', views.create, name='create')
]
