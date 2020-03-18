from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import test, status
from rest_framework.authtoken.models import Token
from .serializers import DashboardSerializer

class TestDashboardsApi(test.APITestCase):
    """
    api/dashboards/
    """
    def setUp(self):
        """
        Create a test user and login. Configure client with token.
        """
        User = get_user_model()
        self.user = User.objects.create_user(email='test@test.com', password='test19931293')
        token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

    def test_create_dashboard(self):
        """
        Ensure the user can create a new dashboard.
        Ensure the response is the dashboard created.
        """
        data = {'url': 'http://www.sjajsjaod.com', 'name': 'Test dashboard name'}
        response = self.client.post(reverse('dashboards'), data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        new_dashboard = DashboardSerializer(self.user.dashboards.filter(name=data['name'])[0])
        self.assertGreaterEqual(response.data.items(), new_dashboard.data.items())

    def test_get_dashboards(self):
        """
        Ensure the user can list all dashboards owned
        """
        response = self.client.get(reverse('dashboards'), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), len(self.user.dashboards.all()))
