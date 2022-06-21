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

    def create(self, validated_data:User):
        try:
            user_already_exists = User.objects.get(email=validated_data["email"])
            if user_already_exists:
                raise KeyError
        except:    
            new_user = User.objects.create_user(**validated_data)
            return new_user    

class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)            

            