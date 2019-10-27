from django.urls import include, path

from authentication.views.signupView import UserSignUp
from authentication.views.verifyView import PhoneVerificationView, activate
from authentication.views.loginView import Login, Profile

app_name = 'authentication'
urlpatterns = [
    path('signup/', UserSignUp.as_view(), name='signup'),
    path('activate/<uidb64>/<token>', activate, name='activate'),
    path('verify/', PhoneVerificationView.as_view(), name='verify'),
    path('login/', Login.as_view(), name='login'),
    path('profile/', Profile.as_view(), name='profile'),
]
