from django import forms
from django.contrib.auth.models import User
from reg.models import UserProfile



class UserForm(forms.ModelForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform avalid email address.')
    password = forms.CharField(widget=forms.PasswordInput())

    allowed = ['itbhu.ac.in', 'iitbhu.ac.in']
    def clean_email(self):

        data = self.cleaned_data['email'].split('@')[-1]
        if data not in self.allowed:   # any check you need
            raise forms.ValidationError("Must be a gmail address")
        return self.cleaned_data['email']

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'first_name', 'last_name')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('college', 'branch', 'year')