from django.urls import path
from django.conf.urls import url
from . import views
# from .views import PersonView

urlpatterns = [
    # Site
    path('', views.index, name='main'),  # здесь мы переходим в функцию index в файле views
    path('<int:pk>', views.index, name='main'),
    path('about', views.about, name='about'),
    path('create', views.create, name='create'),
    # Rest API path
    # path('persons', PersonView.as_view()),
    # path('person', PersonView.as_view()),
    # path('person/<int:pk>', PersonView.as_view()),
    # path('persons/<int:pk>', PersonView.as_view()),
    # Rest API Url
    path('persons/<int:pk>', views.get_persons),
    path('persons', views.all_persons, name='persons'),
    url(r'^person/(?P<pk>[0-9]+)', views.up_del_person),
    path('person', views.creat_persons, name='person'),
]
