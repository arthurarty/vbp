from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.db.utils import IntegrityError
from django.shortcuts import render
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.views import View, generic

from authentication.forms.signUpForm import SignUpForm
from authentication.models import User
from authentication.tokens import account_activation_token
from authentication.utils import send_sms


class UserSignUp(View):
    """
    View to handle user sign up.
    """
    def get(self, request):
        """
        Display form to user
        """
        form = SignUpForm
        return render(request, 'authentication/index.html', {'form': form})

    def post(self, request):
        """
        Handle user data from form
        """
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = User()
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.email = form.cleaned_data['email']
            user.username = form.cleaned_data['email']
            user.dob = form.cleaned_data['dob']
            user.phone_number = form.cleaned_data['phone_number']
            user.set_password(form.cleaned_data['password'])
            user.is_active = False
            try:
                user.save()
            except IntegrityError:
                error = 'Account already exists'
                return render(
                    request, 'authentication/error.html', {'error': error})
            current_site = get_current_site(request)
            mail_subject = 'Verify email'
            context = {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user)
                }
            html_template = render_to_string(
                'authentication/email.html', context
            )
            to_email = user.email
            email = EmailMessage(
                        mail_subject,
                        html_template,
                        from_email='info@me.com',
                        to=[to_email]
            )
            email.content_subtype = 'html'
            email.send()
            context = {
                'user': user,
            }
            return render(request, 'authentication/success.html', context)
        else:
            signup_form = SignUpForm
            return render(
                request, 'authentication/index.html', {
                    'sign_up_errors': form.non_field_errors(),
                    'form': signup_form}
                )
