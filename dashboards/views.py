from rest_framework import views, generics
from rest_framework.response import Response
from .serializers import DashboardSerializer
from .models import Dashboard


class DashboardAPiView(generics.GenericAPIView):
    """
    api/dashboards
    # """
    # def perform_create(self, serializer):
    #     print('CALLED')
    #     serializer.save(owner=self.request.user)

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
