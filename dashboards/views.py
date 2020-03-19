from rest_framework import generics
from rest_framework import views
from rest_framework.response import Response
from .serializers import DashboardSerializer, PageSerializer
from django.shortcuts import get_object_or_404


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


class DashboardPagesRetrieveAPIView(views.APIView):
    """
    Global permissions: IsAuthenticated
    Global authentication: TokenAuthentication

    api/dashboards/<int:dashboard_id>/pages/<int:page_id>/
    """
    def get(self, request, dashboard_id=None, page_id=None):
        if not dashboard_id or not page_id:
            return Response({'error': 'Missing parameters.'})
        dashboard = get_object_or_404(request.user.dashboards.filter(id=dashboard_id))
        page = get_object_or_404(dashboard.pages.filter(id=page_id))
        page_ser = PageSerializer(page)
        return Response(page_ser.data)


class DashboardPagesListAPIView(views.APIView):
    """
    Global permissions: IsAuthenticated
    Global authentication: TokenAuthentication

    api/dashboards/<int:dashboard_id>/pages/
    """
    def get(self, request, dashboard_id=None):
        if not dashboard_id:
            return Response({'error': 'Missing parameters.'})
        dashboard = get_object_or_404(request.user.dashboards.filter(id=dashboard_id))
        page_ser = PageSerializer(dashboard.pages.all(), many=True)
        return Response(page_ser.data)
