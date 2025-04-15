# serializers.py
from rest_framework import serializers
from .models import Movie, Rating, Review

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['id', 'user', 'movie', 'score']

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'movie', 'user', 'username', 'text', 'date']

class MovieSerializer(serializers.ModelSerializer):
    rating = serializers.SerializerMethodField()
    review = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'  # includes all model fields + custom fields like 'rating'

    def get_rating(self, obj):
        return obj.average_rating()

