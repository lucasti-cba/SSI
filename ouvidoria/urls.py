from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.indexo, name ='indexo'),
    path('novaPesquisa', views.novaPesquisa, name ='novaPesquisa'),
    path('novaQuestao/<int:id>/', views.novaQuestao, name ='novaQuestao'),
    path('pesquisa/<int:id>/', views.pesquisa, name ='pesquisa'),

]

