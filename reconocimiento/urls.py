from django.urls import path, include
from . import views

urlpatterns = [
    path('vista_camara', views.vista_camara, name='vista_camara'),
]
