from django.shortcuts import render
from .models import User, UserProfile
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserCreateSerializer, UserProfileSerializer, UserViewSerializer, UserProfileUpdateSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated


@api_view(['POST'])
def create_user(request):
    serializer = UserCreateSerializer(data=request.data)
    response_data = {
        "errors": None,
        "data": None
    }
    if serializer.is_valid():
        user = serializer.save()
        refresh = RefreshToken.for_user(user)

        response_data['data'] = {
            'refresh': str(refresh),
            'access': str(refresh.access_token)

        }
        response_status = status.HTTP_201_CREATED
    else:
        response_data["errors"] = serializer.errors
        response_status = status.HTTP_400_BAD_REQUEST

    return Response(response_data, status=response_status)


@api_view(["GET"])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def user_list(request):
    # protect the view
    # better representation

    users = UserProfile.objects.all()

    serialized_data = UserProfileSerializer(instance=users, many=True)

    return Response(serialized_data.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def get_user(request, pk=None):
    user = UserProfile.objects.filter(id=pk).first()
    # user = UserProfile.objects.get(id=pk)   -> which one is better? filter is better coz filter will send a null value if a object is not present and get will throw an error when object is not present

    if user:
        serializer =UserProfileSerializer(instance=user)
        response_data = {
            "data": serializer.data,
            "error": None
        }
        response_status = status.HTTP_200_OK

    else:
        response_data = {
            "data": None,
            "error": "User doesnt exist"
        }
        response_status = status.HTTP_404_NOT_FOUND

    return Response(response_data, response_status)


@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def update_user_profile(request):
    user_profile_serializer = UserProfileUpdateSerializer(instance=request.user.profile, data=request.data)
    response_data = {
        'data': None,
        'errors': None
    }

    if user_profile_serializer.is_valid():
        user_profile = user_profile_serializer.save()

        response_data['data'] = UserProfileSerializer(instance=user_profile).data
        response_status = status.HTTP_200_OK
    else:
        response_data['errors'] = user_profile_serializer.errors
        response_status = status.HTTP_400_BAD_REQUEST

    return Response(response_data, response_status)
