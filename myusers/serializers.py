from rest_framework.serializers import ModelSerializer, SerializerMethodField
from django.contrib.auth import get_user_model


class UserSerializer(ModelSerializer):

    dashboard_count = SerializerMethodField()

    class Meta:
        model = get_user_model()
        exclude = [
            'last_login',
            'is_superuser',
            'is_staff',
            'groups',
            'user_permissions'
        ]
        # password field will be required to register but
        # will not be sent with the response or retrieval.
        extra_kwargs = {'password': {'write_only': True}}

    def get_dashboard_count(self, user_obj):
        return len(user_obj.dashboards.all())

    def create(self, validated_data):
        user = get_user_model()(email=validated_data['email'])
        user.set_password(validated_data['password'])
        user.save()
        return user
