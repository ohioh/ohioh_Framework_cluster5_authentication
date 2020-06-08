from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
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


class UserRegistrationView(APIView):
    serializer_class = UserPostSerializer

    def post(self, request, *args, **kwargs):
        password = request.data.get('password')
        serializer = UserPostSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.set_password(password)
            user.save()
            return Response({'msg': 'Successfully Registered'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
