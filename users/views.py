from rest_framework.views import APIView, Response
from rest_framework import status
from users.serializers import UserSerializer
from users.models import User

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

