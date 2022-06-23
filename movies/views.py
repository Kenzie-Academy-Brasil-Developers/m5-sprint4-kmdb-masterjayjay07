from django.shortcuts import get_object_or_404
from rest_framework.views import APIView, Response
from rest_framework import status
from movies.serializers import MovieSerializer
from movies.models import Movie
from rest_framework.authentication import TokenAuthentication
from movies.permissions import MyCustomPermission
from kmdb.pagination import CustomPagination

# Create your views here.

class MovieView(APIView, CustomPagination):

    authentication_classes = [TokenAuthentication]
    permission_classes = [MyCustomPermission]

    def get(self, request):
        movies = Movie.objects.all()
        page = self.paginate_queryset(movies, request, view=self)
        serializer = MovieSerializer(page, many=True)   
        return self.get_paginated_response(serializer.data)


   
    def post(self, request):
        # apenas admin
        serializer = MovieSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)





class MovieViewDetail(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [MyCustomPermission]
    
    def get(self, request, movie_id):
        try:
            movie = Movie.objects.get(id=movie_id)
            serializer = MovieSerializer(movie)
            return Response(serializer.data)
        except:
            return Response({"message": "Movie not found."},status=status.HTTP_404_NOT_FOUND)


    def patch(self, request, movie_id):
        # apenas admin
        movie = get_object_or_404(Movie, pk=movie_id)
        serializer = MovieSerializer(movie, request.data, partial=True)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)


    def delete(self, request, movie_id):
        # apenas admin
        movie = get_object_or_404(Movie, pk=movie_id)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)        


