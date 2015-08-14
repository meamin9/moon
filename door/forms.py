# -*- coding:utf-8 -*-
__author__ = 'meamin9'

from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


class RegisterForm(forms.Form):
    username = forms.CharField(label='用户名', max_length=32, min_length=3,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'User name'}))
    password = forms.CharField(label='密码',
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    repassword = forms.CharField(label='确认密码',
                                 widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Repeat Password'}))
    email = forms.EmailField(label='Email',
                             widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))

    def clean_repassword(self):
        if self.cleaned_data.get('password') != self.cleaned_data.get('repassword'):
            raise ValidationError('输入密码不一致', 'repeated')
        return True

    def clean_username(self):
        if User.objects.all().filter(username=self.cleaned_data['username']):
            raise ValidationError('用户名已经被使用', 'unique_username')
        return self.cleaned_data['username']

    def clean_email(self):
        if User.objects.all().filter(email=self.cleaned_data['email']):
            raise ValidationError('邮箱已经注册', 'unique_email')
        return self.cleaned_data['email']
