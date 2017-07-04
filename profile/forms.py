from django import forms
# from django.contrib.auth.forms import UserModel
from django.contrib.auth.forms import UserCreationForm
from profile.models import Profile
from django.contrib.auth.models import User


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "password1", "password2", ]


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'birth_date', 'bio', 'email', ]
