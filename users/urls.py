from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework_simplejwt.views import TokenVerifyView



urlpatterns = [
    path('add/',views.create_user,name = 'create_user_api'),
    path('token/refresh/',TokenRefreshView.as_view(), name = 'token_refresh_api'),

    path('token/verify/', TokenVerifyView.as_view(), name='token_verify_view'),

    path('login/', TokenObtainPairView.as_view(), name='login_api'),
    path('list/', views.user_list, name = "user_list_api"),

    path('<int:pk>/', views.get_user, name= 'get_single_user'),
    #  Path parameter   vs  Query Paramater

    path('update/', views.update_user_profile, name = 'update_user+profile_api'),


]