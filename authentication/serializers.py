from rest_framework import serializers
from .models import User


class UserListSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'developer',
            'public_entity',
            'analyst',
            'grann_pad',
            'email',
        ]


class UserPostSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'developer',
            'public_entity',
            'analyst',
            'grann_pad',
            'email',
            'password'
        ]