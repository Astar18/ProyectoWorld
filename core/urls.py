from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),#root name siempre poner el nombre de la app
    path('about/', views.about, name="about"),
    
    

]