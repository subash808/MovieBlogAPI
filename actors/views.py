from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status

from .models import Actor
from .serializers import ActorSerializer

# Create your views here.

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createActor(request):

    serializer = ActorSerializer(data = request.data)

    if serializer.is_valid():

        actor = serializer.save()

        return Response({
            "status": True,
            "message": 'Actor created successfully.',
            "actor": serializer.data
        }, status = status.HTTP_201_CREATED)

    return Response({
        "status": False,
        "error": serializer.errors
    }, status = status.HTTP_400_BAD_REQUEST)

# Get Actors

@api_view(['GET'])
@permission_classes([AllowAny])
def getActors(request):

    actors = Actor.objects.all().order_by('-id')
    serializer = ActorSerializer(actors, many = True)

    if serializer:
        return Response({
            "status": True,
            "message": 'Actors retrived successfully.',
            "actors": serializer.data
        }, status = status.HTTP_200_OK)

    return Response({
        "status": False,
        "error": serializer.errors
    }, status = status.HTTP_400_BAD_REQUEST)

# GET single actor

@api_view(['GET'])
@permission_classes([AllowAny])
def getActorById(request, id):

    try: 

        actor = Actor.objects.get(id = id)
        serializer = ActorSerializer(actor)

        if serializer:
            return Response({
                "status": True,
                "message": 'Actor retrived successfully.',
                "actor": serializer.data
            }, status = status.HTTP_200_OK)

    except Actor.DoesNotExist:
        return Response({
            "status": False,
            "error": 'Actor not found'
        }, status = status.HTTP_404_BAD_REQUEST)
    
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateActor(request, id):

    try:
        actor = Actor.objects.get(id = id)

    except Actor.DoesNotExist:
        return Response({
            "status": False,
            "error": 'Actor not found.'
        }, status = status.HTTP_404_NOT_FOUND)
    
    serializer = ActorSerializer(actor, data = request.data)

    if serializer.is_valid():
        actor = serializer.save()

        return Response({
            "status": True,
            "message": 'Actor updated successfully.'
        }, status = status.HTTP_200_OK)

    return Response({
        "status": False,
        "error": serializer.errors
    }, status = status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteActor(request, id):

    try:
        actor = Actor.objects.get(id = id)
        actor.delete()

        return Response({
            "status": True,
            "message": 'Actor deleted successfully.'
        }, status.HTTP_200_OK)
    
    except Actor.DoesNotExist:
        return Response({
            "status": False,
            "error": 'Actor not found.'
        }, status.HTTP_404_NOT_FOUND)