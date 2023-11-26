from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
class LoginForm (forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True,widget=forms.PasswordInput)

    # def clean_username(self):
    #     username= self.cleaned_data["username"]
    #     if User.objects.filter(username = username).exists():
    #         return username 
    #     else:
    #         raise forms.ValidationError("this user name not exist")

    def clean(self):
        username= self.cleaned_data["username"]
        if User.objects.filter(username = username).exists():
            pass
        else:
            raise forms.ValidationError("this username not exist")
        
        password = self.cleaned_data["password"]
        user = authenticate(username= username,password =password )
        if user is not None:
            return user
        else:
            raise forms.ValidationError("the  password is in correct")