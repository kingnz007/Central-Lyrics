from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search', views.search, name='search'),
    
    re_path('(?P<artist>.*)/(?P<song>.*)/$', views.lyrics, name='lyrics'),
    
]


