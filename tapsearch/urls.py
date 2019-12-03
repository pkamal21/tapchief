from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.search_list, name='search_list'),
    path('post/', views.text_new, name='text_new'),
]
