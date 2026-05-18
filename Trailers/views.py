from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status

from .models import Trailer
from .serializers import TrailerSerializer


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createTrailer(request):
    serializer = TrailerSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

        return Response({
            "status": True,
            "message": "Trailer created successfully.",
            "trailer": serializer.data
        }, status=status.HTTP_201_CREATED)

    return Response({
        "status": False,
        "errors": serializer.errors
    }, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([AllowAny])
def getTrailers(request):
    trailers = Trailer.objects.all().order_by('-id')
    serializer = TrailerSerializer(trailers, many=True)

    return Response({
        "status": True,
        "trailers": serializer.data
    }, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([AllowAny])
def getTrailer(request, id):
    try:
        trailer = Trailer.objects.get(id=id)
        serializer = TrailerSerializer(trailer)

        return Response({
            "status": True,
            "trailer": serializer.data
        }, status=status.HTTP_200_OK)

    except Trailer.DoesNotExist:
        return Response({
            "status": False,
            "error": "Trailer not found."
        }, status=status.HTTP_404_NOT_FOUND)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateTrailer(request, id):
    try:
        trailer = Trailer.objects.get(id=id)

    except Trailer.DoesNotExist:
        return Response({
            "status": False,
            "error": "Trailer not found."
        }, status=status.HTTP_404_NOT_FOUND)

    serializer = TrailerSerializer(trailer, data=request.data)

    if serializer.is_valid():
        serializer.save()

        return Response({
            "status": True,
            "message": "Trailer updated successfully.",
            "trailer": serializer.data
        }, status=status.HTTP_200_OK)

    return Response({
        "status": False,
        "errors": serializer.errors
    }, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteTrailer(request, id):
    try:
        trailer = Trailer.objects.get(id=id)
        trailer.delete()

        return Response({
            "status": True,
            "message": "Trailer deleted successfully."
        }, status=status.HTTP_200_OK)

    except Trailer.DoesNotExist:
        return Response({
            "status": False,
            "error": "Trailer not found."
        }, status=status.HTTP_404_NOT_FOUND)