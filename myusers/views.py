from django.contrib.auth import get_user_model
from rest_framework import views, response
from .serializers import UserSerializer


class UserApiView(views.APIView):
    """
    Global permissions: IsAuthenticated
    Global authentication: TokenAuthentication

    api/profile/
    """
    def get(self, request):
        serializer = UserSerializer(request.user)
        return response.Response(serializer.data)


class UserRegistrationApiView(views.APIView):
    """
    No permissions or authentication required to register.
    Returns new user info.

    api/register/
    """
    permission_classes = []
    authentication_classes = []

    def post(self, request):
        # Do not use UserSerializer to CREATE new users.
        # User serializer excludes the 'password' field for
        # security reasons and as a result it gets removed from
        # serializer.data.
        User = get_user_model()
        if 'email' not in request.data.keys():
            raise ValueError('Email is required.')
        if 'password' not in request.data.keys():
            raise ValueError('Password is required.')

        # Create the user safely using the create_user() method instead of the serializer option
        new_user = User.objects.create_user(email=request.data['email'], password=request.data['password'])
        # The serializer can be used to LIST/RETRIEVE
        new_user_ser = UserSerializer(new_user)
        return response.Response(new_user_ser.data)
