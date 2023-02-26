from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from blog.models import Blogpost

class SignUpForm(UserCreationForm):
    password1 = forms.CharField(label="Password",widget=forms.PasswordInput(attrs = {"class":'border-2 border-solid border-gray-900 shadow appearance-none border rounded py-2 w-[35.5rem] h-[2rem] px-3 text-gray-700 leading-tight outline-2 outline-green-500'}))
    password2 = forms.CharField(label="Confirm Password",widget=forms.PasswordInput(attrs = {"class":'border-2 border-solid border-gray-900 shadow appearance-none border rounded py-2 w-[35.5rem] h-[2rem] px-3 text-gray-700 leading-tight outline-2 outline-green-500'}))
    class Meta:
        model = User
        fields = ["username","first_name", "last_name", "email"]
        widgets = {
            "username": forms.TextInput(attrs={"class":"border-2 border-solid border-gray-900 shadow appearance-none border rounded py-2 w-[35.5rem] h-[2rem] px-3 text-gray-700 leading-tight outline-2 outline-green-500"}),
            "first_name": forms.TextInput(attrs={"class":"border-2 border-solid border-gray-900 shadow appearance-none border rounded py-2 w-[35.5rem] h-[2rem] px-3 text-gray-700 leading-tight outline-2 outline-green-500"}),
            "last_name": forms.TextInput(attrs={"class":"border-2 border-solid border-gray-900 shadow appearance-none border rounded py-2 w-[35.5rem] h-[2rem] px-3 text-gray-700 leading-tight outline-2 outline-green-500"}),
            "email": forms.TextInput(attrs={"class":"border-2 border-solid border-gray-900 shadow appearance-none border rounded py-2 w-[35.5rem] h-[2rem] px-3 text-gray-700 leading-tight outline-2 outline-green-500"})
            }
        labels = {"first_name": "First Name", "last_name": "Last Name", "email": "Email"}

class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={"autofocus": True, "class":"border-2 border-solid border-gray-900 shadow appearance-none border rounded py-2 w-[35.5rem] h-[2rem] px-3 text-gray-700 leading-tight outline-2 outline-green-500"}))
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password" , "class":"border-2 border-solid border-gray-900 shadow appearance-none border rounded py-2 w-[35.5rem] h-[2rem] px-3 text-gray-700 leading-tight outline-2 outline-green-500"}),
    )

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Blogpost
        fields = ['title', "desc", "author"]
        widgets = {
            "title": forms.TextInput(attrs={"class":"border-2 border-solid border-gray-900 shadow appearance-none border rounded py-2 w-[35.5rem] h-[2rem] px-3 text-gray-700 leading-tight outline-2 outline-green-500"}),
            "desc": forms.Textarea(attrs={"class":"border-2 border-solid border-gray-900 shadow appearance-none border  rounded py-2 w-[35.5rem] h-[5rem] px-3 text-gray-700 leading-tight outline-2 outline-green-500"}),
            "author": forms.TextInput(attrs={"class":"border-2 border-solid border-gray-900 shadow appearance-none border rounded py-2 w-[35.5rem] h-[2rem] px-3 text-gray-700 leading-tight outline-2 outline-green-500"}),
        }


class ContactForm(forms.Form):
    name = forms.CharField(max_length=150, widget=forms.TextInput(attrs={"class": "shadow appearance-none border rounded py-2 w-[35.5rem] h-[2rem] px-3 text-gray-700 leading-tight outline-2 outline-green-500"}))
    email = forms.EmailField(max_length=300, widget=forms.EmailInput(attrs={"class": "shadow appearance-none border rounded py-2 w-[35.5rem] h-[2rem] px-3 text-gray-700 leading-tight outline-2 outline-green-500"}))
    subject = forms.CharField(max_length=500, widget=forms.TextInput(attrs={"class": "shadow appearance-none border rounded py-2 w-[35.5rem] h-[2rem] px-3 text-gray-700 leading-tight outline-2 outline-green-500"}))
    contact = forms.IntegerField(widget=forms.NumberInput(attrs={"class": "shadow appearance-none border rounded py-2 w-[35.5rem] h-[2rem] px-3 text-gray-700 leading-tight outline-2 outline-green-500"}))
    adress = forms.CharField(widget=forms.Textarea(attrs={"class": "border rounded outline-2 outline-green-500 mt-4 h-[3rem] w-[35.5rem] text-gray-700"}))
    message = forms.CharField(widget=forms.Textarea(attrs={"class": "border rounded outline-2 outline-green-500 mt-4 h-[3rem] w-[35.5rem] text-gray-700"}))
    