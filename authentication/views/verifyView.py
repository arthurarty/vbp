from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.views import View

from authentication.models import User, PhoneVerification
from authentication.tokens import account_activation_token
from authentication.utils import send_sms


class PhoneVerificationView(View):
    """
    Class handles verifying phone_number
    """
    def post(self, request):
        user = User.objects.get(
            phone_number=request.POST['phone_number']
            )
        verify = user.phone_verification
        if verify.code == request.POST['code']:
            verify.status = True
            verify.save()
            user.is_active = True
            user.save()
            return redirect('authentication:login')
        return HttpResponse('Invalid code')


def activate(request, uidb64, token):
    """
    method handles email verification
    """
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.save()
        context = {
            'user': user
        }
        no_of_codes = PhoneVerification.objects.filter(user_id=user.id).count()
        if no_of_codes > 0:
            return render(request, 'authentication/error.html', {
                'error': 'Code already sent'})
        send_sms(user)
        return render(
            request, 'authentication/emailVerification.html', context)
    else:
        return HttpResponse('Activation link is invalid!')
