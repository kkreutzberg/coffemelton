from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django import forms


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    # Translate labels, placeholders, and error messages
    username = forms.CharField(
        label=_("Kasutajanimi"),
        help_text=_("Nõutav. Kuni 150 tähemärki. Võib sisaldada ainult tähti, numbreid "
                    "ja @/./+/-/_."),
        # ... other attributes
    )
    email = forms.EmailField(
        label=_("E-maili aadress"),
        help_text=_("Sisestage kehtiv e-maili aadress."),
        # ... other attributes
    )
    password1 = forms.CharField(
        label=_("Salasõna"),
        help_text=_(
            "Salasõna peab sisaldama vähemalt 8 tähemärki ja 2 numbrit või sümbolit. "
            "Salasõna ei tohi olla liialt sarnane isiklike andmetega."),
        widget=forms.PasswordInput,
        # ... other attributes
    )
    password2 = forms.CharField(
        label=_("Salasõna kinnitus"),
        help_text=_(
            "Sisestage sama salasõna uuesti veendumaks, et sisestamisel ei tekkinud "
            "vigu."),
        widget=forms.PasswordInput,
        # ... other attributes
    )

    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)
        self.fields['email'].required = True

    def clean_username(self):
        username = self.cleaned_data['username']

        if User.objects.filter(username=username).exists():
            raise forms.ValidationError(
                _("See kasutajanimi on juba võetud. Palun vali mõni teine kasutajanimi.")
            )

        return username

    def clean_email(self):
        email = self.cleaned_data.get("email")

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(
                _("Sellise meiliaadressiga kasutaja on juba olemas.")
            )

        if len(email) >= 350:
            raise forms.ValidationError("Meiliaadress on liiga pikk. ")

        return email


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(
        label=_("Kasutajanimi"),
        widget=forms.TextInput,
        # ... other attributes
    )
    password = forms.CharField(
        label=_("Salasõna"),
        widget=forms.PasswordInput,
        # ... other attributes
    )

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

    username = forms.CharField(
        label=_("Kasutajanimi"),
        help_text=_("Nõutav. Kuni 150 tähemärki. Võib sisaldada ainult tähti, numbreid "
                    "ja @/./+/-/_."),
        # ... other attributes
    )
    email = forms.EmailField(
        label=_("E-maili aadress"),
        help_text=_("Nõutav. Sisestage kehtiv e-maili aadress."),
        # ... other attributes
    )
