from rest_framework.serializers import ModelSerializer, SerializerMethodField
from django.contrib.auth import get_user_model


class UserSerializer(ModelSerializer):

    dashboard_count = SerializerMethodField()

    class Meta:
        model = get_user_model()
        exclude = [
            'password',
            'last_login',
            'is_superuser',
            'is_staff',
            'groups',
            'user_permissions'
        ]

    def get_dashboard_count(self, user_obj):
        return len(user_obj.dashboards.all())
