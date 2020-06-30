from django import forms
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
    nickname=forms.CharField(max_length=20)
    email=forms.EmailField(label="이메일")