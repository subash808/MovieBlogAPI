from django.contrib.auth import authenticate
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from rest_framework_simplejwt.token_blacklist.models import BlacklistedToken, OutstandingToken
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework.permissions import IsAuthenticated, AllowAny

from .serializers import RegisterSerializer, LoginSerializer, UserSerializer

# Create your views here.

@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):

    serializer = RegisterSerializer(data = request.data)

    if serializer.is_valid():

        user = serializer.save()

        return Response({
            "status": True,
            "message": 'User created successfully.',
            "user": UserSerializer(user).data
        }, status = status.HTTP_201_CREATED)

    return Response({
        "status": False,
        "error": serializer.errors
    }, status = status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):

    serializer = LoginSerializer(data = request.data)

    if serializer.is_valid():

        email = serializer.validated_data['email']
        password = serializer.validated_data['password']

        user = authenticate(username = email, password = password)

        if user is None:

            return Response({
                "status": False,
                "error": 'Invalid credential.'
            }, status = status.HTTP_401_UNAUTHORIZED)
        
        token = RefreshToken.for_user(user)

        return Response({
            "status": True,
            "message": 'User logged in successfully.',
            "token": {
                "refresh": str(token),
                "access": str(token.access_token)
            },
            "user": UserSerializer(user).data
        }, status = status.HTTP_200_OK)

    return Response({
        "status": False,
        "error": serializer.errors
    }, status = status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logOut(request):

    refreshToken = request.data.get('refresh')

    if not refreshToken:
        return Response({
            "status": False,
            "error": 'Refresh Token is required.'
        }, status.HTTP_400_BAD_REQUEST)
    
    try:
        token = RefreshToken(refreshToken)

        token.blacklist()

        raw_access = request.auth
        jti = raw_access['jti']
        outstanding = OutstandingToken.objects.get(jti=jti)
        BlacklistedToken.objects.get_or_create(token=outstanding)

        return Response({
            "status": True,
            "message": 'Logged out successfully.'
        }, status.HTTP_200_OK)
    
    except OutstandingToken.DoesNotExist:
        # Access token not in outstanding list, just return success
        return Response({
            "status": True,
            "message": 'Logged out successfully.'
        }, status.HTTP_200_OK)

    except TokenError:
        return Response({
            "status": False,
            "error": 'Invalid or expired Token',
        }, status.HTTP_400_BAD_REQUEST)

    except Exception as e:
        return Response({
            "status": True,
            "error": str(e)
        }, status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def profile(request):

    serializer = UserSerializer(request.user)

    return Response({
        "status": True,
        "user": serializer.data
    }, status = status.HTTP_200_OK)