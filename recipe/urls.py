from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('recipe/<int:id>/', views.recipe_detail, name='recipe_detail'),
]