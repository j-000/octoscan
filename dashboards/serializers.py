from rest_framework import serializers
from .models import Dashboard


class DashboardSerializer(serializers.ModelSerializer):
    pages_count = serializers.SerializerMethodField()

    class Meta:
        model = Dashboard
        exclude = ['owner']

    def get_pages_count(self, dashboard_obj):
        return len(dashboard_obj.pages.all())
