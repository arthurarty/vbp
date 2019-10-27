from django.test import Client
from django.urls import reverse
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode

from authentication.models import User
from authentication.tokens import account_activation_token
from tests.sample_data.auth import user_1, user_2, user_4, user_5
from tests.base import BaseTestCase


class AuthSignUpTests(BaseTestCase):
    def test_sign_up_display(self):
        """
        Sign Up route should display form
        """
        response = self.client.get(reverse('authentication:signup'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Create an Account!")
        self.assertTemplateUsed(response, 'authentication/index.html')

    def test_post_sign_up(self):
        """
        Ensure post creates user that is not active
        """
        response = self.signup_user(user_1)
        user = User.objects.get(email=user_1['email'])
        self.assertEqual(response.status_code, 200)
        self.assertEqual(user.is_active, False)

    def test_activation(self):
        """
        Ensure user can activate using link provided
        """
        response = self.signup_user(user_1)
        user = User.objects.get(email=user_1['email'])
        token = account_activation_token.make_token(user)
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        response = self.verify_user(uid, token)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Email Verified.")

    def test_invalid_user_activation(self):
        """
        User that does not exist in system should return error
        """
        token = 'afsfagib134312glsfsda#@'
        uid = 465
        response = self.verify_user(uid, token)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Activation link is invalid!")

    def test_password_mismatch(self):
        """
        Exception should be raised when a user creates a password
        and fails to repeat it.
        """
        response = self.signup_user(user_2)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Phone numbers do not match")

    def test_phone_number_mismatch(self):
        """
        Exception should be raised when a user creates a phone_number
        and fails to repeat it.
        """
        response = self.signup_user(user_2)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Passwords do not match")

    def test_dob_wrong_format(self):
        """
        Date of birth should be provided in the format mm/dd/yyy
        Test ensures user gets error message.
        """
        response = self.signup_user(user_4)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Invalid format: date of birth')

    def test_dob_below_18(self):
        """
        Test ensures under age people cannot create account.
        """
        response = self.signup_user(user_5)
        self.assertEqual(response.status_code, 200)
        self.assertContains(
            response, 'Service is not available to persons under 18.')

    def test_duplicate_account(self):
        """
        Test ensures duplicate phone_number or email error
        is handled
        """
        self.signup_user(user_1)
        response = self.signup_user(user_1)
        self.assertEqual(response.status_code, 200)
        self.assertContains(
            response, 'Account already exists')
        self.assertTemplateUsed(response, 'authentication/error.html')
