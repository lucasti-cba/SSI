from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.internacao, name ='internacao'),
    path('soro/', views.soro, name ='soro'),
    path('view/', views.internacaoV, name ='internacaoV'),
    path('add_internacao', views.add_internacao, name='add_internacao'),
    path('add_soro/', views.add_soro, name='add_soro'),
    path('edit_internacao', views.add_internacao, name='edit_internacao'),
    path('alta_internacao', views.add_internacao, name='alta_internacao'),
    path('delete_internacao/<int:id>', views.delete_internacao, name='delete_internacao'),
    path('edit_internacao/<int:id>', views.edit_internacao, name='edit_internacao'),
    path('colorPI/<int:id>', views.colorPI, name='colorPI'),
    path('livre/<int:id>', views.livre_internacao, name='livre_internacao'),
    path('update', views.atualiza_painel, name='atualiza_painel'),
    path('reservado/<int:id>', views.reservado_internacao, name='reservado_internacao')

]

