from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name ='nutri'),
    path('cardapio/', views.cardapio, name ='cardapio'),
    path('card_edit/', views.card_edit, name ='card_edit'),
    path('novarefe/<int:id>', views.novarefe, name='novarefe'),
    path('delete_ali/<int:id>/<int:alimento>', views.removeAlimento, name="delete_ali"),
    path('delete_card/<int:id>/', views.removeCardapio, name="delete_card"),
    ]