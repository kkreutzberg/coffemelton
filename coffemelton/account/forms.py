from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django import forms

from django.forms.widgets import PasswordInput, TextInput


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)
        self.fields['email'].required = True

    def clean_email(self):
        email = self.cleaned_data.get("email")

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("We already have an user with this e-mail")

        if len(email) >= 350:
            raise forms.ValidationError("E-mail is way too long. ")

        return email


class LoginUserForm(AuthenticationForm):
    class Meta:
        username = forms.CharField(widget=TextInput())
        password = forms.CharField(widget=PasswordInput())

    def __init__(self, *args, **kwargs):
        super(LoginUserForm, self).__init__(*args, **kwargs)


class UpdateUserForm(forms.ModelForm):
    password = None

    def __init__(self, *args, **kwargs):
        super(UpdateUserForm, self).__init__(*args, **kwargs)
        self.fields['email'].required = True

    class Meta:
        model = User
        fields = ['username', 'email']
        exclude = ['password1', 'password2']
