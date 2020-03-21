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
        """
        Create user using the serializer methods.
        """
        user = UserSerializer(data=request.data)
        if user.is_valid():
            user.save()
            return response.Response(user.data)
        return response.Response(user.errors)
