from django import forms
import re
from myShopSales.models import User

class UserLoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(),required=False)
    username = forms.CharField(widget=forms.TextInput(),required=False)
    repassword = forms.CharField(widget=forms.PasswordInput(),required=False)

    class Meta():
        model = User
        fields =('username','password','email')



class LoginForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput(), required=False)
    username = forms.CharField(widget=forms.TextInput(), required=False)


