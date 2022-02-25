from django.urls import path
from . import views

urlpatterns = [
    path('get-comic/', views.getData),
    path('add-comic/', views.addComic),
    path('comic-update/<str:pk>/', views.comicUpdate, name="comic-update"),
    path('comic-delete/<str:pk>/', views.comicDelete, name="comic-delete"),

]
