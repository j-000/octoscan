from rest_framework import test, status
from rest_framework.authtoken.models import Token
from django.urls import reverse
from django.contrib.auth import get_user_model
from .serializers import UserSerializer
from django.shortcuts import get_object_or_404


class ObtainTokenTest(test.APITestCase):
    """
    api/login
    """

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
    """
    api/profile
    """

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


class UserRegistrationTest(test.APITestCase):
    """
    api/register
    """

    def test_user_registration(self):
        """
        Ensure we can register and that response
        only contains authorized fields
        """
        data = {'email': 'test@test.com', 'password': 'test67jss72h'}
        response = self.client.post(reverse('register'), data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        new_user = UserSerializer(get_object_or_404(get_user_model().objects.filter(email=data['email'])))
        # Assert the response is a subset of the user object dict
        self.assertGreaterEqual(new_user.data.items(), response.data.items())

        prohibited_fields = ['password', 'is_staff', 'user_permissions', 'is_superuser']
        for field in prohibited_fields:
            self.assertNotIn(field, response.data.keys())