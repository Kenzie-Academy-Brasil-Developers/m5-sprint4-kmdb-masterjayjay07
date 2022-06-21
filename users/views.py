from rest_framework.views import APIView, Response, status
from users.serializers import UserSerializer, UserLoginSerializer
from users.models import User
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate

# Create your views here.

class UserView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        try:
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except KeyError:
            return Response({"email": ["email already exists"]}, status=status.HTTP_400_BAD_REQUEST)


class UserLoginView(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(
            username=serializer.validated_data["email"],
            password=serializer.validated_data["password"],
        )

        if user:
            token = Token.objects.get_or_create(user=user)[0]
            return Response({"token": token.key}, status=status.HTTP_200_OK)
        return Response(
            {"detail": "invalid email or password"}, status.HTTP_401_UNAUTHORIZED
        )
