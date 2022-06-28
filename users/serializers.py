from rest_framework import serializers
from users.models import User

class UserSerializer(serializers.Serializer):
    id           = serializers.IntegerField(read_only=True)
    email        = serializers.EmailField()
    first_name   = serializers.CharField(max_length=50)
    last_name    = serializers.CharField(max_length=50)
    password     = serializers.CharField(write_only=True)
    date_joined  = serializers.DateTimeField(read_only=True)
    updated_at   = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)            

            