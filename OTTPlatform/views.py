from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status

from .models import OTTPlatform
from .serializers import OTTPlatformSerializer


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createOTT(request):
    serializer = OTTPlatformSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

        return Response({
            "status": True,
            "message": "OTT platform created successfully.",
            "ott": serializer.data
        }, status=status.HTTP_201_CREATED)

    return Response({
        "status": False,
        "errors": serializer.errors
    }, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([AllowAny])
def getOTTs(request):
    otts = OTTPlatform.objects.all().order_by('-id')
    serializer = OTTPlatformSerializer(otts, many=True)

    return Response({
        "status": True,
        "otts": serializer.data
    }, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([AllowAny])
def getOTTById(request, id):
    try:
        ott = OTTPlatform.objects.get(id=id)
        serializer = OTTPlatformSerializer(ott)

        return Response({
            "status": True,
            "ott": serializer.data
        }, status=status.HTTP_200_OK)

    except OTTPlatform.DoesNotExist:
        return Response({
            "status": False,
            "error": "OTT platform not found."
        }, status=status.HTTP_404_NOT_FOUND)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateOTT(request, id):
    try:
        ott = OTTPlatform.objects.get(id=id)

    except OTTPlatform.DoesNotExist:
        return Response({
            "status": False,
            "error": "OTT platform not found."
        }, status=status.HTTP_404_NOT_FOUND)

    serializer = OTTPlatformSerializer(ott, data=request.data)

    if serializer.is_valid():
        serializer.save()

        return Response({
            "status": True,
            "message": "OTT platform updated successfully.",
            "ott": serializer.data
        }, status=status.HTTP_200_OK)

    return Response({
        "status": False,
        "errors": serializer.errors
    }, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteOTT(request, id):
    try:
        ott = OTTPlatform.objects.get(id=id)
        ott.delete()

        return Response({
            "status": True,
            "message": "OTT platform deleted successfully."
        }, status=status.HTTP_200_OK)

    except OTTPlatform.DoesNotExist:
        return Response({
            "status": False,
            "error": "OTT platform not found."
        }, status=status.HTTP_404_NOT_FOUND)