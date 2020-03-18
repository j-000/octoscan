from rest_framework import generics
from rest_framework.response import Response
from .serializers import DashboardSerializer


class DashboardAPiView(generics.GenericAPIView):
    """
    Global permissions: IsAuthenticated
    Global authentication: TokenAuthentication

    api/dashboards/
    """
    def get(self, request):
        """
        List all user's dashboards
        """
        user_dashboards = self.request.user.dashboards.all()
        serializer = DashboardSerializer(user_dashboards, many=True)
        return Response(serializer.data)

    def post(self, request):
        """
        Create a new dashboard
        """
        request.data.update({'owner': request.user.id})
        dash = DashboardSerializer(data=request.data)
        if dash.is_valid():
            dash.save()
            return Response(dash.data)
        return Response(dash.errors)


class DashboardRetrieveAPIView(generics.RetrieveAPIView):
    """
    Global permissions: IsAuthenticated
    Global authentication: TokenAuthentication

    api/dashboards/<int:pk>
    """
    serializer_class = DashboardSerializer

    def get_queryset(self):
        return self.request.user.dashboards.all()
