from django.contrib.auth.models import User
from django import forms
import django.contrib.auth.password_validation as validators
from captcha.fields import CaptchaField

class CaptchaTestForm(forms.Form):
    captcha = CaptchaField()

class AxesCaptchaForm(forms.Form):
    captcha = CaptchaField()

class UserCreationForm1(forms.ModelForm):
    """
    A form that creates a user, with no privileges, from the given username and
    password.
    """
    error_messages = {
        'password_mismatch': ("The two password fields didn't match."),
    }
    password1 = forms.CharField(label= ("Password"),
        widget=forms.PasswordInput)
    password2 = forms.CharField(label= ("Password confirmation"),
        widget=forms.PasswordInput,
        help_text= ("Enter the same password as above, for verification."))

    class Meta:
        model = User
        fields = ("username",)

    def username_check(self, uservalue):
        try:
            test = User.objects.get(username=uservalue)
            return True
        except Exception:
            return False

    def clean_password2(self):
        password1 = self.data.get("password1")
        password2 = self.data.get("password2")
        if password1 and password2 and password1 != password2:
            return False
        return True

    def save1(self, commit=True):
        user = super(UserCreationForm1, self).save(commit=False)
        user.set_password(self.data["password1"])
        if commit:
            user.save()
        return user