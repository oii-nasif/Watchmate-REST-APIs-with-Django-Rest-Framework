from django.urls import path

from watchlist_app.api.views import (WatchListAV, WatchListDetailAV, StreamPlatformAV, WatchListGV,
                                    StreamPlatformDetailAV, ReviewList, ReviewDetail, UserReview, ReviewCreate)
# from watchlist_app.api.views import WatchListAV, WatchListDetailAV, StreamPlatformAV, StreamPlatformDetailAV


urlpatterns = [
    path('list/', WatchListAV.as_view(), name='movie-list'),
    path('<int:pk>/', WatchListDetailAV.as_view(), name='movie-detail'),
    path('list2/', WatchListGV.as_view(), name='watch-list'),

    path('stream/', StreamPlatformAV.as_view(), name='stream-list'),
    path('stream/<int:pk>/', StreamPlatformDetailAV.as_view(), name='streamplatform-detail'),
    
    path('<int:pk>/review-create/', ReviewCreate.as_view(), name='review-create'),
    path('<int:pk>/review/', ReviewList.as_view(), name='review-list'),
    path('review/<int:pk>/', ReviewDetail.as_view(), name='review-detail'),
    
    # path('review/<str:username>/', UserReview.as_view(), name='user-review-detail'),
    path('review/', UserReview.as_view(), name='user-review-detail'),
]
