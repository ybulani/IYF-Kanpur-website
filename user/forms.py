from django import forms
from .models import Profile, Brother
from django.forms import ModelForm, CharField, inlineformset_factory
from django.contrib.auth.hashers import make_password,is_password_usable,check_password
import string
import random
from django.forms import BaseModelFormSet
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import MinimumLengthValidator, validate_password, password_validators_help_text_html
from django.shortcuts import render,redirect
from datetime import datetime
from django.http import HttpResponseRedirect, HttpResponse,QueryDict
from django.contrib.auth.forms import UserCreationForm
from django.forms import formset_factory
# import datetime


def current_year():
    return datetime.today().year

def year_choices():
    return [(r,r) for r in range(1960, datetime.today().year+1)]
    

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean(self):
       cleaned_data=super(UserRegisterForm,self).clean()
       email = self.cleaned_data.get('email')
       if User.objects.filter(email=email).exists():
            msg = "Email already exists"
            self.add_error('email',msg)
            # raise ValidationError("Email exists")
       return self.cleaned_data

       
# class SignupForm(ModelForm):
#   verify_password = forms.CharField(label="Type your password to verify ",widget=forms.PasswordInput(), max_length=100)
#   class Meta:
#       model = User
#       fields = ['username','password','verify_password','email']
#       widgets = {
#           'password':forms.PasswordInput(),
#       }
#   def clean(self):
#       #rewriting clean method to check whether passwords match or not
#       cleaned_data=super(SignupForm,self).clean()
#       username=cleaned_data.get('username')
#       email=cleaned_data.get('email')
#       ps1=cleaned_data.get('password')
#       ps2=cleaned_data.get('verify_password')
#       if email=="":
#           self.add_error('email',"Please input your email!")
#       if ps1!=ps2:
#           msg="Password does not match!"
#           self.add_error('verify_password',msg)
#       # Save hashed password instead of password directly
#       encoded_password=make_password(ps1,make_salt())
#       cleaned_data['password']=encoded_password
#       # Make sure email is unique
#       if email and User.objects.filter(email=email).exclude(username=username).count():
#           msg="Email has been used!"
#           self.add_error('email',msg)
#       # Validate password
#       if ps1:
#           try:
#               validate_password(ps1,user=self)
#               cleaned_data['help_text']=None
#           except ValidationError:
#               cleaned_data['help_text']=password_validators_help_text_html()
#               self.add_error('password','Your password it too weak. Please choose another password')
#       return cleaned_data

        
class SigninForm(forms.Form):
    username = forms.CharField(label="User name ",required=False, max_length=100)
    email=forms.EmailField(label="Your email ", required=False, max_length=100)
    password = forms.CharField(label="Password ", widget=forms.PasswordInput(), max_length=100)
    def clean(self):
        cleaned_data=super(SigninForm,self).clean()
        username=cleaned_data.get("username")
        email=cleaned_data.get("email")
        password=cleaned_data.get("password")
        if not (username or email):
            msg="Please input your user name or email!"
            self.add_error('username',msg)
        lookup=None
        if username:
            if User.objects.filter(username=username).count()==0:
                msg="Username does not exist!"
                self.add_error('username',msg)
            elif not authenticate(username=username,password=password):
                msg="User name and password does not match!"
                self.add_error('password',msg)
        else:
            if User.objects.filter(email=email).count()==0:
                msg="Email does not exist!"
                self.add_error('email',msg)
            elif not authenticate(username=email,password=password):
                msg="Email and password does not match!"
                self.add_error('password',msg)
        return cleaned_data



def make_salt():
    ###Your code here
    letters=string.ascii_letters
    result=random.sample(letters,5)
    return ''.join(result)


class CreateProfileModelForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['user','image','blood_group','dob','gender','marital_status']

class BrotherForm(forms.ModelForm):
    # brother_name = forms.CharField(
    #     label='Brother Name',
    #     widget=forms.TextInput(attrs={
    #         'class': 'form-control',
    #         'placeholder': 'Enter Brother\'s name here'
    #     })
    # )
    year_of_birth = forms.TypedChoiceField(coerce=int, choices=year_choices, initial=current_year)
    class Meta:
        model = Brother
        fields = ['brother_name','year_of_birth']
        # exclude = ()



BrotherFormSet = inlineformset_factory(Profile, Brother, form=BrotherForm, extra=2)


class UserUpdateForm(forms.ModelForm):
    # email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username']#['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']



# class CustomerProfileForm(forms.ModelForm):

#     class Meta:
#         model = CustomerProfile
#         fields = '__all__'
#         exclude = ('customer_username',)