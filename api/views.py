from gc import collect
from pickle import GET
from typing import Collection
from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Comic
from base.models import UserCollection
from .serializers import CollectionSerializer, ComicSerializer
from rest_framework import generics


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/comic-list/',
        'Detail': '/comic-detail/',
        'Create': '/comic-create/',
        'Update': '/comic-update/<str:pk>/',
    }


@api_view(['GET'])
def comicList(request):
    comics = Comic.objects.all()
    serializer = ComicSerializer(comics, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def comicDetail(request, pk):
    comics = Comic.objects.get(id=pk)
    serializer = ComicSerializer(comics, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def addComic(request):
    serializer = ComicSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['PUT'])
def comicUpdate(request, pk):
    comic = Comic.objects.get(id=pk)
    serializer = ComicSerializer(instance=comic, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def comicDelete(request, pk):
    comic = Comic.objects.get(id=pk)
    comic.delete()

    return Response('Item succsesfully deleted!')


@api_view(['GET'])
def getCollection(request, pk):
    collection = UserCollection.objects.get(id=pk)
    serializer = CollectionSerializer(instance=collection)
    print(serializer)
    return Response(serializer.data)


@api_view(['POST'])
def collectionCreate(request):
    serializer = CollectionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


class CollectionCreate(generics.CreateAPIView):
    # API endpoint that allows creation of a new customer
    queryset = UserCollection.objects.all(),
    serializer_class = CollectionSerializer


class CollectionList(generics.RetrieveAPIView):
    # API endpoint that allows customer to be viewed.
    queryset = UserCollection.objects.all()
    serializer_class = CollectionSerializer


class CollectionUpdate(generics.RetrieveUpdateAPIView):
    # API endpoint that allows a customer record to be updated.
    queryset = UserCollection.objects.all()
    serializer_class = CollectionSerializer


class CollectionDelete(generics.RetrieveDestroyAPIView):
    # API endpoint that allows a customer record to be deleted.
    queryset = UserCollection.objects.all()
    serializer_class = CollectionSerializer
