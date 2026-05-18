from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status

from .models import Series
from .serializers import SeriesSerializer


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createSeries(request):
    serializer = SeriesSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

        return Response({
            "status": True,
            "message": "Series created successfully.",
            "series": serializer.data
        }, status=status.HTTP_201_CREATED)

    return Response({
        "status": False,
        "errors": serializer.errors
    }, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([AllowAny])
def getSeriesList(request):
    series = Series.objects.all().order_by('-id')
    serializer = SeriesSerializer(series, many=True)

    return Response({
        "status": True,
        "series": serializer.data
    }, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([AllowAny])
def getSeries(request, id):
    try:
        item = Series.objects.get(id=id)
        serializer = SeriesSerializer(item)

        return Response({
            "status": True,
            "series": serializer.data
        }, status=status.HTTP_200_OK)

    except Series.DoesNotExist:
        return Response({
            "status": False,
            "error": "Series not found."
        }, status=status.HTTP_404_NOT_FOUND)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateSeries(request, id):
    try:
        item = Series.objects.get(id=id)

    except Series.DoesNotExist:
        return Response({
            "status": False,
            "error": "Series not found."
        }, status=status.HTTP_404_NOT_FOUND)

    serializer = SeriesSerializer(item, data=request.data)

    if serializer.is_valid():
        serializer.save()

        return Response({
            "status": True,
            "message": "Series updated successfully.",
            "series": serializer.data
        }, status=status.HTTP_200_OK)

    return Response({
        "status": False,
        "errors": serializer.errors
    }, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteSeries(request, id):
    try:
        item = Series.objects.get(id=id)
        item.delete()

        return Response({
            "status": True,
            "message": "Series deleted successfully."
        }, status=status.HTTP_200_OK)

    except Series.DoesNotExist:
        return Response({
            "status": False,
            "error": "Series not found."
        }, status=status.HTTP_404_NOT_FOUND)