from django.urls import path
from .views import *

urlpatterns = [
    path('', personas_carga, name='cargar'),
    path('cargar/', carga_simple, name='carga-simple'),
]
