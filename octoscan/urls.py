from django.contrib import admin
from django.urls import path
from myusers.views import UserApiView
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('api/auth/', obtain_auth_token, name='api_token_auth'),
    # path('api/users/', UserApiViewCreate.as_view()),
    path('api/profile/', UserApiView.as_view(), name='profile'),
    path('admin/', admin.site.urls),
]
