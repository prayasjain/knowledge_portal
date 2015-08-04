__author__ = 'PRAYAS'

from django import forms
from login.models import UserProfile

class loginform(forms.ModelForm) :

    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput(),max_length=128)
    fullname = forms.CharField(max_length=256)
    email = forms.EmailField()
    contact = forms.IntegerField()
    linkedin = forms.CharField()
    user_type = forms.CharField()
    user_interests = forms.CharField()
    education = forms.CharField()

    class Meta :
        model = UserProfile
        fields = ('username','password','fullname','email','contact','linkedin','user_type','user_interests','education')

class account_loginform(forms.Form):

    username = forms.CharField()
    password =forms.CharField(widget=forms.PasswordInput())

