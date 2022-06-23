from rest_framework import serializers
from reviews.models import Review
from users.serializers import UserSerializer
from movies.models import Movie


class CriticSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()


class ReviewSerializer(serializers.ModelSerializer):
    critic = CriticSerializer(read_only=True)
    class Meta:
        model = Review
        fields = ["id", "stars", "review", "spoilers", "movie", "critic", "recomendation"]
        

    def create(self, validated_data:dict):
        critic = validated_data.pop("critic")
        movie = validated_data.pop("movie")
        actual_movie = Movie.objects.get(pk=movie)
        review = Review.objects.create(**validated_data, critic=critic, movie=actual_movie)
        review.recomendation = review.get_recomendation_display()
        return review
    