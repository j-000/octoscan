from rest_framework import generics
from rest_framework import views
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .serializers import DashboardSerializer, PageSerializer


class DashboardAPiView(generics.ListCreateAPIView):
    """
    Global permissions: IsAuthenticated
    Global authentication: TokenAuthentication

    api/dashboards/
    """

    serializer_class = DashboardSerializer

    def get_queryset(self):
        user = self.request.user
        return user.dashboards.all()

    def post(self, request, *args, **kwargs):
        """
        Overridden post method to include extra details in the post data
        before saving.
        Create a new dashboard.
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
    Returns a single dashboard instance based on <int:pk>
    """
    serializer_class = DashboardSerializer

    def get_queryset(self):
        """
        Automatically filter the user dashboards against <int:dashboard_id>
        based on the QuerySet of all the user's dashboards.

        Could have alternatively overridden .get_object() but would
        have to implement the object permissions.
        """
        return self.request.user.dashboards.all()


class DashboardPagesRetrieveAPIView(generics.RetrieveAPIView):
    """
    Global permissions: IsAuthenticated
    Global authentication: TokenAuthentication

    api/dashboards/<int:dashboard_id>/pages/<int:page_id>/
    """
    serializer_class = PageSerializer

    def get_queryset(self):
        """
        Filter the user dashboards against <int:dashboard_id> and then filter
        the dashboard pages against <int:page_id> and return its details.
        """
        dashboard_id = self.kwargs['dashboard_id']
        page_id = self.kwargs['page_id']
        dashboard = get_object_or_404(self.request.user.dashboards.filter(id=dashboard_id))
        return get_object_or_404(dashboard.pages.filter(id=page_id))


class DashboardPagesListAPIView(generics.ListAPIView):
    """
    Global permissions: IsAuthenticated
    Global authentication: TokenAuthentication

    api/dashboards/<int:dashboard_id>/pages/
    """
    serializer_class = PageSerializer

    def get_queryset(self):
        """
        Filter the user dashboards against <int:dashboard_id>
        and then return all its pages.
        """
        dashboard_id = self.kwargs['dashboard_id']
        dashboard = get_object_or_404(self.request.user.dashboards.filter(id=dashboard_id))
        return dashboard.pages.all()
