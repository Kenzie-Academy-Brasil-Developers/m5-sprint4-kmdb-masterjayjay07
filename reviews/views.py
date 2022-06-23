from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView, Response
from reviews.models import Review
from reviews.serializers import ReviewSerializer
from movies.models import Movie
from reviews.permissions import MyCustomPermission,OwnerPermission
from users.models import User

# Create your views here.
class ReviewView(APIView):
    def get(self, request):
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)



class ReviewDetailView(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, OwnerPermission]

    def delete(self, request, review_id):
        review = get_object_or_404(Review, pk=review_id)
        critic = User.objects.get(id=review.critic.id)
        self.check_object_permissions(request,critic)
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class ReviewMovieView(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [MyCustomPermission]

    def get(self, request, movie_id):
        get_object_or_404(Movie, pk=movie_id) 
        reviews = Review.objects.filter(movie=movie_id)
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)

    def post(self, request, movie_id):
        get_object_or_404(Movie, pk=movie_id)        
        serializer = ReviewSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save(movie=movie_id, critic = request.user)
        return Response(serializer.data,status=status.HTTP_201_CREATED)
                   
