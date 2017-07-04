from django import forms
# from django.contrib.auth.forms import UserModel
from django.contrib.auth.forms import UserCreationForm
from profile.models import Profile
from django.contrib.auth.models import User


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "password1", "password2",]

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'birth_date', 'bio', 'email',]















"""class SignUpForm(UserCreationForm):
    birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')
    bio = forms.TextInput()


    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'birth_date', 'email', 'password1', 'password2', 'bio', )

    username = forms.CharField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    birth_date = forms.DateField()#help_text='Required. Format: YYYY-MM-DD')
    bio = forms.TextInput()
    email = forms.EmailField()
    password = forms.CharField()
    password2 = forms.CharField()"""

"""class Meta:
        model = Profile
        widgets = {'birth_date': forms.DateInput(attrs={'class': 'datepicker'})}
        fields = ('first_name', 'last_name', 'birth_date', 'bio', 'email')
        #fields = ('username', 'first_name', 'last_name', 'birth_date', 'bio', 'password1', 'password2', )"""
