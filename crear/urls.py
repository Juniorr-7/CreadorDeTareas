from django.urls import path
from .views import *

urlpatterns = [
    path('',listar,name='listar'),
    path('creacion',creacion,name='creacion')
]