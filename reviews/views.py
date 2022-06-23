from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView, Response
from reviews.models import Review
from reviews.serializers import ReviewSerializer


# Create your views here.
class ReviewView(APIView):
    def get(self, request):
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)



class ReviewDetailView(APIView):
    def delete(self, request):
        ...


class ReviewMovieView(APIView):

    authentication_classes = [TokenAuthentication]

    def get(self, request):
        ...

    def post(self, request, movie_id):
        # new = {
        #     "movie":movie_id,
        #     "critic":request.user,
        #     **request.data
        # }        
        serializer = ReviewSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save(movie=movie_id, critic = request.user)
        return Response(serializer.data)
                   
