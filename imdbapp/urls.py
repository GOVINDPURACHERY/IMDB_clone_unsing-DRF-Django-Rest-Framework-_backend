from imdbapp import views
from django.urls import path
from .views import *

urlpatterns = [
    path('movielist/',WatchListAV.as_view(), name='movie_list'),
    path('moviedetailview/<int:pk>/', WatchDetailAV.as_view(), name='movie_detail'),
    path('streamplatformlist/',StreamPlatformAV.as_view(), name='stream_platform_list'),
    path('streamplatformdetail/<int:pk>/',StreamPlatformDetailAV.as_view(),name= 'stream_platform_detail'),

    # path('streamplatformlist/<int:pk>/review', ReviewList.as_view(), name='rview-list'),
    # path('streamplatformlist/review/<int:pk>', ReviewDetail.as_view(), name='review_detail'),
        

    path('<int:pk>/reviews/',ReviewList.as_view(), name='review_list'),
    path('review/<int:pk>/',ReviewDetail.as_view(), name='review_detail'),
    path('<int:pk>/reviewcreate/',ReviewCreate.as_view(), name='review_create'),


]   