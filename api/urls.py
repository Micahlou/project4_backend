from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name="api-overview"),
    path('comic-list/', views.comicList, name="comic-list"),
    path('comic-detail/<str:pk>/', views.comicDetail, name="comic-detail"),
    path('comic-create/', views.addComic),
    path('comic-update/<str:pk>/', views.comicUpdate, name="comic-update"),
    path('comic-delete/<str:pk>/', views.comicDelete, name="comic-delete"),
    # path('collection-list/str:<pk>/', views.getCollection, name="collection-list"),
    path('collection/create/', views.CollectionCreate.as_view(),
         name="collection-create"),

    path('collection/list/<str:pk>/',
         views.CollectionList.as_view(), name='collectionList'),
    path('collection/update/<str:pk>/',
         views.CollectionUpdate.as_view(), name='collectionUpdate'),
    path('collection/delete/<str:pk>/',
         views.CollectionDelete.as_view(), name='collectionDelete')



]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
