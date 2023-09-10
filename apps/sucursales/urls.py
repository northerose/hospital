from django.urls import path
from apps.sucursales import views


urlpatterns = [
    path('', views.sucursales, name='sucursales'),
            ]