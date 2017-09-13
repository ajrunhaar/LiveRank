"""
Definition of forms.
"""

from django import forms
#from django.contrib.auth.models import User
from app.models import Player

from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))

class RegistrationForm(forms.ModelForm):
    first_name=forms.CharField(widget=forms.TextInput(
        attrs={
            'name':"signup_firstname",
            'id':"firstname_id",
            'class':"form-control input-lg",
            'placeholder':"First Name",
        }
    ))
    last_name=forms.CharField(widget=forms.TextInput(
        attrs={
            'name':"signup_lastname",
            'id':"lastname_id",
            'class':"form-control input-lg",
            'placeholder':"Last Name",
        }
    ))
    username=forms.CharField(widget=forms.TextInput(
        attrs={
            'name':"signup_email",
            'id':"username_id",
            'class':"form-control input-lg",
            'placeholder':"E-mail",
        }
    ))
    contact=forms.CharField(widget=forms.TextInput(
        attrs={
            'name':"signup_contact",
            'id':"contact_id",
            'class':"form-control input-lg",
            'placeholder':"Contact Number [10 Digit]",
            'pattern':"^\d{10}$"
        }
    ))
    password = forms.CharField(widget=forms.PasswordInput(
                attrs={
            'name':"signup_password",
            'id':"password_id",
            'class':"form-control input-lg",
            'placeholder':"Password",
        }
    ))
    class Meta:
        model=Player
        fields=('first_name','last_name','username','contact','password')

class LoginForm(forms.ModelForm):
   
    username=forms.CharField(widget=forms.TextInput(
        attrs={
            'name':"signup_email",
            'id':"username_id",
            'class':"form-control input-lg",
            'placeholder':"E-mail",
        }
    ))

    password = forms.CharField(widget=forms.PasswordInput(
                attrs={
            'name':"signup_password",
            'id':"password_id",
            'class':"form-control input-lg",
            'placeholder':"Password",
        }
    ))
    class Meta:
        model=Player
        fields=('username','password')