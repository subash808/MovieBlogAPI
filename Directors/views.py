from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status

from .models import Directors
from .serializers import DirectorsSerializers

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createDirector(request):

    serializer = DirectorsSerializers(data = request.data)

    if serializer.is_valid():
        director = serializer.save()

        return Response({
            "status": True,
            "message": 'Director created successfully.',
            "director": serializer.data
        }, status.HTTP_201_CREATED)
    else:
        return Response({
            "status": False,
            "error": serializer.errors
        }, status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
@permission_classes([AllowAny])
def getDirectors(request):

    directors = Directors.objects.all().order_by('-id')
    serializer = DirectorsSerializers(directors, many = True)

    if serializer:
        return Response({
            "status": True,
            "message": 'Directors retrieved successfully.',
            "directors": serializer.data
        }, status.HTTP_200_OK)

    return Response({
        "status": False,
        "error": serializer.errors
    }, status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([AllowAny])
def getDirectorById(request, id):

    try:

        director = Directors.objects.get(id = id)
        serializer = DirectorsSerializers(director)

        if serializer:
            return Response({
                "status": True,
                "message": 'Director retrieved successfully.',
                "director": serializer.data
            }, status.HTTP_200_OK)
        else:
            return Response({
                "status": False,
                "error": serializer.errors
            }, status.HTTP_400_BAD_REQUEST)
        
    except Directors.DoesNotExist:
        return Response({
            "status": False,
            "error": 'Director not found.'
        }, status.HTTP_404_NOT_FOUND)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateDirector(request, id):

    try: 
        director = Directors.objects.get(id = id)

    except Directors.DoesNotExist:
        return Response({
            "status": False,
            "error": 'Director not found.'
        }, status.HTTP_404_NOT_FOUND)
    
    serializer = DirectorsSerializers(director, data = request.data)

    if serializer.is_valid():
        serializer.save()

        return Response({
            "status": True,
            "message": 'Director updated successfully.'
        }, status.HTTP_200_OK)
    
    else:
        return Response({
            "status": False,
            "error": serializer.errors
        }, status.HTTP_400_BAD_REQUEST)
    
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteDirector(request, id):

    try:
        director = Directors.objects.get(id = id)

    except Directors.DoesNotExist:
        return Response({
            "status": False,
            "error": 'Director not found.'
        }, status.HTTP_404_NOT_FOUND)
    
    if director:
        director.delete()

        return Response({
            "status": True,
            "message": 'Director deleted successfully.'
        }, status.HTTP_200_OK)
    
    else:
        return Response({
            "status": False,
            "error": 'Error occurs while deleting director.'
        }, status.HTTP_500_INTERNAL_SERVER_ERROR)