from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status

from .models import Movies
from .serializers import MovieSerializer


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createMovie(request):
    serializer = MovieSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

        return Response({
            "status": True,
            "message": "Movies created successfully.",
            "movie": serializer.data
        }, status=status.HTTP_201_CREATED)

    return Response({
        "status": False,
        "errors": serializer.errors
    }, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([AllowAny])
def getMovies(request):
    movies = Movies.objects.all().order_by('-id')
    serializer = MovieSerializer(movies, many=True)

    return Response({
        "status": True,
        "movies": serializer.data
    }, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([AllowAny])
def getMovie(request, id):
    try:
        movie = Movies.objects.get(id=id)
        serializer = MovieSerializer(movie)

        return Response({
            "status": True,
            "movie": serializer.data
        }, status=status.HTTP_200_OK)

    except Movies.DoesNotExist:
        return Response({
            "status": False,
            "error": "Movies not found."
        }, status=status.HTTP_404_NOT_FOUND)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateMovie(request, id):
    try:
        movie = Movies.objects.get(id=id)

    except Movies.DoesNotExist:
        return Response({
            "status": False,
            "error": "Movies not found."
        }, status=status.HTTP_404_NOT_FOUND)

    serializer = MovieSerializer(movie, data=request.data)

    if serializer.is_valid():
        serializer.save()

        return Response({
            "status": True,
            "message": "Movies updated successfully.",
            "movie": serializer.data
        }, status=status.HTTP_200_OK)

    return Response({
        "status": False,
        "errors": serializer.errors
    }, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteMovie(request, id):
    try:
        movie = Movies.objects.get(id=id)
        movie.delete()

        return Response({
            "status": True,
            "message": "Movies deleted successfully."
        }, status=status.HTTP_200_OK)

    except Movies.DoesNotExist:
        return Response({
            "status": False,
            "error": "Movies not found."
        }, status=status.HTTP_404_NOT_FOUND)