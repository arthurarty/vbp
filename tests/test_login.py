from django.urls import reverse

from authentication.models import User
from tests.base import BaseTestCase
from tests.sample_data.auth import user_1


class TestLogin(BaseTestCase):
    """
    Test user login
    """

    def test_login_page(self):
        """
        Ensure login page loads with right template
        """
        response = self.client.get(reverse('authentication:login'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Welcome")
        self.assertTemplateUsed(response, 'authentication/login.html')

    def test_user_login(self):
        """
        Ensure user can login
        """
        self.signup_user(user_1)
        user = User.objects.get(email=user_1['email'])
        user.is_active = False
        user.save()
        response = self.client.post(reverse('authentication:login'), data={
            'email': user_1['email'],
            'password': user_1['password']
        })
        self.assertEqual(response.status_code, 200)

    def test_user_login_fail(self):
        """
        Users who do not exist should not be able to login
        """
        response = self.client.post(reverse('authentication:login'), data={
            'email': user_1['email'],
            'password': user_1['password']
        })
        self.assertContains(
            response, "Username and password didn't match")
