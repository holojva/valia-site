from django import forms
from news.models import UserInformation

from django.contrib.auth import get_user_model

User = get_user_model()
class ProfileModelForm(forms.ModelForm):
    class Meta:
        model = UserInformation
        fields = [
            "bio",
            "profile_image"
        ]
class LoginForm(forms.Form) :
    username = forms.CharField(label="Your name:")
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form__password"

            }
        )
    )
    def clean_username(self) :
        profile = self.cleaned_data.get("username")
        queryset = User.objects.filter(username__iexact=profile)

        if not queryset.exists():
            raise forms.ValidationError("Wrong username or password")
        return profile
class RegisterForm(forms.Form):
    username = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form__password"
            }
        )
    )
    def clean_username(self) :
        profile = self.cleaned_data.get("username")
        queryset = User.objects.filter(username__iexact=profile)
        if queryset.exists():
            raise forms.ValidationError("Your name is stupid, choose another")
        return profile