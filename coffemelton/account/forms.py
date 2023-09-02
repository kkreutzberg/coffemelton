from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
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

    old_password = forms.CharField(
        label='Kehtiv salasõna',
        widget=forms.PasswordInput,
        required=False  # Not required if the user wants to update other profile information only
    )
    new_password1 = forms.CharField(
        label='Uus salasõna',
        widget=forms.PasswordInput,
        required=False
    )
    new_password2 = forms.CharField(
        label='Kinnita uus salasõna',
        widget=forms.PasswordInput,
        required=False
    )

    confirm_delete = forms.BooleanField(
        label="Soovin konto kustutada",
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    class Meta:
        model = User
        fields = ['username', 'email', 'old_password', 'new_password1', 'new_password2']
        # exclude = ['password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(UpdateUserForm, self).__init__(*args, **kwargs)
        self.fields['email'].required = True

    def clean_old_password(self):
        old_password = self.cleaned_data.get('old_password')
        if old_password and not self.instance.check_password(old_password):
            raise forms.ValidationError('Incorrect old password.')
        return old_password

    def clean(self):
        cleaned_data = super().clean()
        new_password1 = cleaned_data.get('new_password1')
        new_password2 = cleaned_data.get('new_password2')

        if new_password1 and new_password2 and new_password1 != new_password2:
            raise forms.ValidationError('Kirjuta uus parool kaks korda ühtmoodi!')

        return cleaned_data

