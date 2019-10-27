from django import forms
from utils.date import convert_date_string, calculate_age


class SignUpForm(forms.Form):
    """
    Form for signing up
    """
    first_name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control form-control-user',
                'placeholder': 'Enter first name',
            }
        ))
    last_name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control form-control-user',
                'placeholder': 'Enter last name',
            }
        )
    )
    email = forms.CharField(
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control form-control-user',
                'placeholder': 'Enter email address',
            }
        ))
    phone_number = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control form-control-user',
                'placeholder': 'Enter phone number',
            }
        ))
    phone_number2 = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control form-control-user',
                'placeholder': 'Repeat phone number',
            }
        ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control form-control-user',
            'placeholder': 'Password',
        }
        ))
    repeatPassword = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control form-control-user',
            'placeholder': 'Repeat Password'
        }
    ))
    dob = forms.CharField(
        label='Date of birth',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control form-control-user',
                'placeholder': 'Enter Date of birth dd/mm/yyyy',
            }
        ))

    def clean(self):
        cleaned_data = super().clean()

        password1 = cleaned_data.get("password")
        password2 = cleaned_data.get("repeatPassword")

        phone_number = cleaned_data.get("phone_number")
        phone_number2 = cleaned_data.get("phone_number2")

        dob = cleaned_data.get("dob")

        errors_list = []

        try:
            cleaned_data['dob'] = convert_date_string(dob)
            age = calculate_age(cleaned_data['dob'])
            if age < 18:
                errors_list.append(forms.ValidationError(
                    'Service is not available to persons under 18.'
                ))
        except ValueError:
            errors_list.append(forms.ValidationError(
                'Invalid format: date of birth'
                ))

        if phone_number != phone_number2:
            errors_list.append(forms.ValidationError(
                ('Phone numbers do not match'), code='phone_number'))

        if password1 != password2:
            errors_list.append(forms.ValidationError(
                ('Passwords do not match'), code='password'))

        if len(errors_list) > 0:
            raise forms.ValidationError(errors_list)
        return cleaned_data
