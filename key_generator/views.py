import jwt
from datetime import datetime
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from auth.settings import SECRET_KEY
from key_generator.models import GeneratedKey
from authentication.models import User
from .serializers import AccessKeySerializer


class GenerateKeyView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user = request._user

        if not user.permission_granted:
            return Response({'msg': 'Admin not permitted you yet'}, status=status.HTTP_400_BAD_REQUEST)
        
        key_payload = {
            'username': user.username,
            'developer': user.developer,
            'public_entity': user.public_entity,
            'analyst': user.analyst,
            'grann_pad': user.grann_pad,
            'datetime': str(datetime.utcnow())
        }

        access_key = jwt.encode(key_payload, SECRET_KEY, algorithm='HS256')
        try:
            user = User.objects.get(username=user.username)
            obj, created = GeneratedKey.objects.update_or_create(
                user=user,
                defaults={'access_key': access_key, 'last_update': datetime.now()}
            )
        except User.DoesNotExist:
            return Response({'msg': 'User not found'}, status=status.HTTP_404_NOT_FOUND)


        return Response({'api_access_key': access_key})


class GetUserAccessKeyView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = self.request._user

        if not user.permission_granted:
            return Response({'msg': 'Admin not permitted you yet'}, status=status.HTTP_400_BAD_REQUEST)

        generated_key = GeneratedKey.objects.filter(user__username=user.username).first()
        serializer = AccessKeySerializer(generated_key)
        return Response(serializer.data)
