from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.text_new, name='text_new'),
]
