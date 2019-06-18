
from django import forms
from .models import MyUser
from django.utils.translation import gettext_lazy


class LoginForm(forms.Form):
    email=forms.EmailField(label='邮箱')
    username=forms.CharField(label='用户名')
    password=forms.CharField(label='密码',widget=forms.PasswordInput)



class MyUserLoginForm(forms.ModelForm):
    class Meta():
        model=MyUser
        fields=['username','password']
        widgets={'password':forms.PasswordInput}
        help_texts={'username':gettext_lazy('')}
class MyUserRegisterForm(forms.ModelForm):
    class Meta():
        model=MyUser
        fields=['username','password','email']
        widgets={'password':forms.PasswordInput(attrs={'placeholder':'请输入密码'}),
                 'email':forms.EmailInput(attrs={'placeholder':'请输入邮箱'}),
                 'username':forms.TextInput(attrs={'placeholder':'请输入账号','required':False}),

                 }
        help_texts={'username':gettext_lazy('')}




