from django.urls import path
from . import views

urlpatterns = [
    path('', views.getData),
    path('add/', views.addComic),
    path('comic-update/<str:pk>/', views.comicUpdate, name="comic-update"),
    path('comic-delete/<str:pk>/', views.comicDelete, name="comic-delete"),

]
