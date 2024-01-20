from rest_framework import serializers
from imdbapp.models import StreamPlatform, WatchList, Review

class ReviewSerializer(serializers.ModelSerializer):
    review_user = serializers.StringRelatedField(read_only=True) #here review user is not completely exluded drom serializer, it just avoided during post operation,working in get operation. thats why did not completely excluded like watchlist.instead it is seperatly mentioned in seralizer and make it read only.
    class Meta:
        model = Review
        # fields = '__all__'
        exclude = ('watchlist',) # Here watchlist or movie details is completely removing from get and post operations, so it is excluded from serializer.
        #but it is included in models, so stored the particular movie id in models/data table

class WatchListSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True) #reviews is the related name given in the model field description, 
    '''read only means it will neglected during post operaion, but it will work during get operation.'''
    class Meta:
        model = WatchList
        fields = '__all__'

class StreamPlatformSerializer(serializers.ModelSerializer):
    watchlist = WatchListSerializer(many=True, read_only=True) #For nested serializers to reated many to one relations
    class Meta:
        model = StreamPlatform
        fields = '__all__'

'''note:
        review serializer gives only review data,
        watchlist serializer include movie details+review data
        streamplatformserializer gives stream platform details+movie details+review details

        here using foreign key relation we take the other model class datas into required model classes.
        related name in models.py is important for creating this relationship
'''