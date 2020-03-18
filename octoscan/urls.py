from django.contrib import admin
from django.urls import path
from myusers import views as myusers_views
from dashboards import views as dashboards_views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    # App views
    path('api/login/', obtain_auth_token, name='api_token_auth'),
    path('api/register/', myusers_views.UserRegistrationApiView.as_view(), name='register'),
    path('api/profile/', myusers_views.UserApiView.as_view(), name='profile'),
    path('api/dashboards/', dashboards_views.DashboardAPiView.as_view(), name='dashboards'),

    # Django admin area
    path('admin/', admin.site.urls),
]
