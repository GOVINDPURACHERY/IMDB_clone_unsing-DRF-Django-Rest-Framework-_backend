from rest_framework import serializers
from imdbapp.models import StreamPlatform, WatchList, Review

class ReviewSerializer(serializers.ModelSerializer):
    review_user = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Review
        # fields = '__all__'
        exclude = ('watchlist',)

class WatchListSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True) #reviews is the related name given in the model field description, 
    '''read only means it will neglected during post operaion, but it will work during get operation'''
    class Meta:
        model = WatchList
        fields = '__all__'

class StreamPlatformSerializer(serializers.ModelSerializer):
    watchlist = WatchListSerializer(many=True, read_only=True) #For nested serializers to reated many to one relations
    class Meta:
        model = StreamPlatform
        fields = '__all__'

