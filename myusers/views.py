from django.contrib.auth import get_user_model
from rest_framework import views, response
from .serializers import UserSerializer


User = get_user_model()


class UserApiView(views.APIView):
    """
    Global permissions: IsAuthenticated
    Global authentication: TokenAuthentication
    """

    def get(self, request):
        serializer = UserSerializer(request.user)
        return response.Response(serializer.data)

    def post(self, request):
        return response.Response()


# class UserApiView(generics.RetrieveAPIView):
#     permission_classes = [IsSelfPermission]
#     serializer_class = UserSerializer
#     queryset = User.objects.all()
#
#
# class UserApiViewCreate(generics.CreateAPIView):
#     serializer_class = UserSerializer
