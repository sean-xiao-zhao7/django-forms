from django.urls import path
from .views import ReviewView, ThankyouView, ReviewListView, SingleReviewView, FavoriteReview

urlpatterns = [
    path("", ReviewView.as_view()),
    path('thankyou', ThankyouView.as_view()),
    path('reviewlist', ReviewListView.as_view()),
    path('single-review/favorite', FavoriteReview.as_view()),
    path('single-review/<int:pk>', SingleReviewView.as_view()),    
]
