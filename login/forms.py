from django import forms

class UserForm(forms.Form):
    """用户表单"""
    username = forms.CharField(label='用户名', max_length=128)
    password = forms.CharField(label='密码', max_length=256, widget=forms.PasswordInput)