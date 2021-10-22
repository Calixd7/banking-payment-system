from rest_framework import serializers
from core.models import * 

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            'pk',
            'username',
            'name',
            'email',
            'password'
        ]

