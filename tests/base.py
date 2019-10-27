import json

import httpretty
from django.test import Client, TestCase
from django.urls import reverse

from authentication.models import User


class BaseTestCase(TestCase):
    """
    All helper methods
    """

    @httpretty.activate
    def verify_user(self, uid, token):
        """
        Method verifies user it is given
        by sending post request to signup
        endpoint
        """
        httpretty.register_uri(
            httpretty.POST, "https://api.sandbox.africastalking.com/version1/messaging",
            body=json.dumps({"hello": "world"}))
        return self.client.get(reverse(
            'authentication:activate', kwargs={
                'uidb64': uid,
                'token': token
                }))

    def signup_user(self, user):
        """
        Sign up given user
        """
        return self.client.post(reverse(
            'authentication:signup'), user)

    def activate_user(self, user):
        """
        Activate a given user
        """
        user = User.objects.get(email=user['email'])
        user.is_active = True
        user.save()
        return user
