from rest_framework import serializers
from .models import User

class RegisterSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only = True)

    class Meta: 
        model = User
        fields = (
            'id', 'username', 'phoneNo', 'email', 'password', 'role'
        )

    def create(self, validated_data):

        user = User.objects.create_user(
            username = validated_data['username'],
            phoneNo = validated_data['phoneNo'],
            email = validated_data['email'],
            password = validated_data['password'],
            role = validated_data.get('role', 'user')
        )

        return user
    
class LoginSerializer(serializers.Serializer):

    email = serializers.EmailField()
    password = serializers.CharField()

class UserSerializer(serializers.ModelSerializer):

    class Meta:

        model = User
        fields = (
            'id', 'username', 'phoneNo', 'email', 'password', 'role'
        )