from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from .models import User
from .serializers import UserListSerializer, UserPostSerializer


class UserListView(generics.ListCreateAPIView):
    permission_classes = [IsAdminUser]

    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return UserPostSerializer
        return UserListSerializer


class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserPostSerializer
