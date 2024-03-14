from django.urls import path
from .import views


# Create a post / update a post
# Upload media
# View the post - feed, post_detail

# Every image/video is uploaded individually using the upload media endpoints
# The post object is created with no media/caption because it is needed as reference


urlpatterns = [
    path('', views.UserPostCreateFeed.as_view(), name='user_post_view'),
    path('media/', views.PostMediaView.as_view(), name='post_media_view'),
    path('<int:pk>/', views.UserPostDetailUpdateView.as_view(), name='post_detail_update'),




]