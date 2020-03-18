from rest_framework.serializers import ModelSerializer
from django.contrib.auth import get_user_model


class UserSerializer(ModelSerializer):
    class Meta:
        model = get_user_model()
        exclude = ['password', 'last_login', 'is_superuser', 'is_staff', 'groups', 'user_permissions']

        def get_dashboards_count(self, user_obj):
            return len(user_obj.dashboards.all())
