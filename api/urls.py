from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from . import views

urlpatterns = [
    path('', views.getData),
    path('add/', views.addComic),
    path('comic-update/<str:pk>/', views.comicUpdate, name="comic-update"),
    path('comic-delete/<str:pk>/', views.comicDelete, name="comic-delete"),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
