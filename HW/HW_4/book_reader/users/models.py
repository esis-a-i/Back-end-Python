from django.db import models
from django import forms


class user(models.Model):

    first_name = models.CharField(max_length=64, verbose_name='First name')

    last_name = models.CharField(max_length=64, verbose_name='Last name')

    password = forms.CharField(
        widget=forms.PasswordInput, verbose_name='Password')

    email = models.EmailField(verbose_name='Email')

    class Meta:
        ordering = ['first_name']
