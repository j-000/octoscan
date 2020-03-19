from rest_framework import serializers
from .models import Dashboard, PageModel


class DashboardSerializer(serializers.ModelSerializer):
    pages_count = serializers.SerializerMethodField()

    class Meta:
        model = Dashboard
        fields = '__all__'
        # This excludes owner from the response or retrieve
        extra_kwargs = {'owner': {'write_only': True}}

    def get_pages_count(self, dashboard_obj):
        return len(dashboard_obj.pages.all())


class PageSerializer(serializers.ModelSerializer):

    class Meta:
        model = PageModel
        fields = '__all__'

