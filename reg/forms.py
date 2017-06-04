from django import forms
from django.contrib.auth.models import User
from reg.models import UserProfile



class UserForm(forms.ModelForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform avalid email address.')
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'first_name', 'last_name')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('college', 'branch', 'year')