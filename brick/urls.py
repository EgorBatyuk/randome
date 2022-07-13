from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create_context/', views.index, name='create_context'),
]