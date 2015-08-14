# -*- coding:utf-8 -*-
__author__ = 'meamin9'

from django import forms


class RegisterInfo(forms.Form):
    username = forms.CharField(label='用户名', max_length=32, min_length=3,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'User name'}))
    password = forms.CharField(label='密码',
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    email = forms.EmailField(label='Email',
                             widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    # repassword = forms.CharField(label='confirm', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
