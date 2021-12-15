
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('provas/', views.pro),
    path('conteudos/', views.conteudos),
    path('Cursos', views.cursos),
    path('simulados/', views.simul),
    path('disciplinas/', views.Matema),
    path('Redacaos/', views.Redac),
]









