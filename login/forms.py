__author__ = 'PRAYAS'

from django import forms
from login.models import UserProfile

class loginform(forms.ModelForm) :
    password = forms.CharField(widget=forms.PasswordInput())

    class meta :
        model = UserProfile
        exclude= ()
