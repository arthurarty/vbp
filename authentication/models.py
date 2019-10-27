import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models
from utils.date import calculate_age


class User(AbstractUser):
    """Custom user class to include phone number
    and change username field to email
    """
    email = models.EmailField(unique=True)
    phone_number = models.CharField(unique=True, max_length=12)
    dob = models.DateField('date of birth')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['dob', 'password', 'phone_number', 'username']

    @property
    def phone_verification(self):
        """return the phone_verification object"""
        return PhoneVerification.objects.get(user=self.id)

    @property
    def age(self):
        """return age of user"""
        return calculate_age(self.dob)


class PhoneVerification(models.Model):
    """Phone verification table"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=255)
    status = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
