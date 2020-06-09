from rest_framework import serializers
from .models import GeneratedKey


class AccessKeySerializer(serializers.ModelSerializer):

    class Meta:
        model = GeneratedKey
        fields = [
            'access_key',
            'last_update'
        ]