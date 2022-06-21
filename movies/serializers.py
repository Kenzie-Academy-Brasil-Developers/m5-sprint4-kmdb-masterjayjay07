from rest_framework import serializers
from genres.serializers import GenreSerializer
from genres.models import Genre
from movies.models import Movie

class MovieSerializer(serializers.Serializer):
    id             = serializers.IntegerField(read_only=True)
    title          = serializers.CharField(max_length=127)
    premiere       = serializers.DateField()
    duration       = serializers.CharField(max_length=10)
    classification = serializers.IntegerField()
    synopsis       = serializers.CharField()

    genres = GenreSerializer(many=True)

    def create(self, validated_data:dict):
        genres_data = validated_data.pop("genres")
        genres = []
        for g in genres_data:
            genre = Genre.objects.get_or_create(**g)[0]
            genres.append(genre)
        movie = Movie.objects.create(**validated_data)
        movie.genres.set(genres)
        return movie