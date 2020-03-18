from rest_framework import test, status
from rest_framework.authtoken.models import Token
from django.urls import reverse
from django.contrib.auth import get_user_model
from .serializers import UserSerializer

class ObtainTokenTest(test.APITestCase):

    def setUp(self):
        """
        Create test user
        """
        User = get_user_model()
        self.user = User.objects.create_user(email='test@test.com', password='test19931293')

    def test_get_token(self):
        """
        Ensure we can get an auth token
        """
        data = {'username': 'test@test.com', 'password': 'test19931293'}
        response = self.client.post(reverse('api_token_auth'), data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class UserProfileTest(test.APITestCase):

    def setUp(self):
        """
        Create user and generate an authentication token
        """
        User = get_user_model()
        self.user = User.objects.create_user(email='test@test.com', password='test19931293')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_get_profile(self):
        """
        Ensure we can get the user's profile info only
        """
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # serialize the user model and check the response is a subset of the dictionary
        user = UserSerializer(self.user)
        self.assertGreaterEqual(user.data.items(), response.data.items())
