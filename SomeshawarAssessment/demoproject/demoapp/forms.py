from django import forms
from .models import Registration
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


CHOICES = [('male','male'),('female','female')]
COUNTRIES = [('India','India'),('America','America'),('Japan','Japan')]

class RegistrationForm(forms.Form):
    name = forms.CharField(max_length=23, label='Name')
    dob = forms.DateField(label='DOB')
    email = forms.EmailField(label='Email Id')
    phone = forms.CharField(max_length=12, min_length=10, label='Phone Number')
    gender = forms.ChoiceField(choices=CHOICES, label='Gender', widget=forms.RadioSelect())
    flat = forms.IntegerField(label='Flat No')
    street = forms.CharField(max_length=45, label='Street')
    country = forms.ChoiceField(choices=COUNTRIES, label='Country', widget=forms.Select())
    img = forms.ImageField(label='Upload Photo')

'''
CHOICES = [('male','male'),('female','female')]
COUTRIES = [('india','india'),('America','America'),('Japan','Japan'),('China','China')]

class RegistrationForm(UserCreationForm):
    name = forms.CharField(max_length=23, label='Name')
    dob = forms.DateField(label='DOB')
    email = forms.EmailField(label='Email Id')
    phone = forms.CharField(max_length=12, min_length=10, label='Phone Number')
    gender = forms.ChoiceField(choices=CHOICES,label='Gender', widget=forms.RadioSelect())
    flat = forms.IntegerField(label='Flat No')
    street = forms.CharField(max_length=45,label='Street')
    country = forms.ChoiceField(choices=COUTRIES,label='Country', widget=forms.Select())
    img = forms.ImageField(label='Upload Photo')

    class Meta:
        model = User
        fields = ['name','dob','email','phone','gender','flat','street','country','img']
        #exclude = ['password','password confirmation']
'''