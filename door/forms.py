__author__ = 'meamin9'

from django import forms


class RegisterInfo(forms.Form):
    email = forms.EmailField(label='Email', widget=forms.TextInput(attrs={'class': 'form-control',
                                                                          'placeholder': 'Email'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                                   'placeholder': 'Password'}))
    # repassword = forms.CharField(label='confirm', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    # name = forms.CharField(max_length=32, min_length=3, widget=forms.TextInput(attrs={'class': 'form-control'}))
