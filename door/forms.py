__author__ = 'meamin9'

from django import forms


class RegisterInfo(forms.Form):
    email = forms.EmailField(label='Email')
    password = forms.CharField(widget=forms.PasswordInput)
    repassword = forms.CharField(label='confirm', widget=forms.PasswordInput)
    name = forms.CharField(max_length=32, min_length=3)
