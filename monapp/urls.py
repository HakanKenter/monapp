from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="accueil"),
    path('user/<int:id>', views.user, name="user"),
    path('person/', views.person, name="person"), 
]