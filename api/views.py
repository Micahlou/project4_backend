from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Comic
from .serializers import ComicSerializer


@api_view(['GET'])
def getData(request):
    comics = Comic.objects.all()
    serializer = ComicSerializer(comics, many=True)
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
