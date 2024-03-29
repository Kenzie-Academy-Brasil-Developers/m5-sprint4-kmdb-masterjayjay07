from rest_framework.views import APIView, Response, status
from users.serializers import UserSerializer, UserLoginSerializer
from users.models import User
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework.authentication import TokenAuthentication
from users.permissions import MyCustomPermission
from kmdb.pagination import CustomPagination

# Create your views here.

class UserView(APIView, CustomPagination):
    
    authentication_classes = [TokenAuthentication]
    permission_classes = [MyCustomPermission]

    def post(self, request):
        try:
            user_already_exists = User.objects.get(email=request.data["email"])
            if user_already_exists:
                return Response({"email": ["email already exists"]}, status=status.HTTP_400_BAD_REQUEST)
        except:
            serializer = UserSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
    
    def get(self, request):    
        # apenas admin
        users = User.objects.all()
        page = self.paginate_queryset(users, request, view=self)
        serializer = UserSerializer(page, many=True)
        return self.get_paginated_response(serializer.data) 



class UserViewDetail(APIView):
    # apenas admin
    authentication_classes = [TokenAuthentication]
    permission_classes = [MyCustomPermission]
    def get(self, request, user_id):
        try:
            user = User.objects.get(id=user_id)
            serializer = UserSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response({"message": "User not found."},status=status.HTTP_404_NOT_FOUND)   



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
