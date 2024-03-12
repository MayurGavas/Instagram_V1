from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from .models import UserProfile
from rest_framework import serializers

class UserCreateSerializer(ModelSerializer):

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        user = User.objects.create(**validated_data)
        UserProfile.objects.create(user=user)

        return user

    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'first_name')

class UserViewSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ('first_name','last_name','email')


class UserProfileSerializer(ModelSerializer):

    user = UserViewSerializer()

    class Meta:
        model = UserProfile
        fields = ('bio', 'profile_pic_url', 'user',)
        # exclude = ('id','is_verified')


class UserProfileUpdateSerializer(ModelSerializer):

    first_name = serializers.CharField()
    last_name = serializers.CharField()

    def update(self, instance, validated_data):
        user = instance.user
        user.first_name = validated_data.pop('first_name')
        user.last_name = validated_data.pop('last_name')

        user.save()

        instance.bio = validated_data.get('bio', None)
        instance.profile_pic_url = validated_data.get('profile_pic_url', None)
        instance.save()

        return instance

    class Meta:
        model = UserProfile
        fields = ('first_name','last_name','bio','profile_pic_url')



