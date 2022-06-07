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
    username = forms.CharField(label="Имя пользователя:")
    password = forms.CharField(label="Пароль:",
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
            raise forms.ValidationError("Неправильное имя пользователя или пароль")
        return profile
class RegisterForm(forms.Form):
    username = forms.CharField(required=True, label="Имя пользователя:" )
    email = forms.EmailField(required=True, label="Почта:")
    password = forms.CharField(label="Пароль:",
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
            raise forms.ValidationError("Такое имя пользователя уже есть.")
        return profile