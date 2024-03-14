from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import UserPost, PostMedia
from .serializers import UserPostCreateSerializer, PostMediaCreateSerializer
from rest_framework import mixins


# Create your views here.
class UserPostCreateFeed(mixins.CreateModelMixin, generics.GenericAPIView):
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [JWTAuthentication, ]
    queryset = UserPost.objects.all()
    serializer_class = UserPostCreateSerializer

    def get_serializer_context(self):
        return {'current_user': self.request.user.profile}

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


# Post creation view

# create post with just the author id
# upload media files with the reference of post id obtained in the last step
# update the post and publish it

class PostMediaView(mixins.CreateModelMixin, generics.GenericAPIView):
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [JWTAuthentication, ]
    serializer_class = PostMediaCreateSerializer

    def put(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class UserPostDetailUpdateView(mixins.UpdateModelMixin, generics.GenericAPIView):
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [JWTAuthentication, ]
    serializer_class = UserPostCreateSerializer
    queryset = UserPost.objects.all()

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
