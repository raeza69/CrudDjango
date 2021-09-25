from django import forms
from .models import Product, Location, Movement
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)


class LocationForm(forms.ModelForm):
    name = forms.CharField(label='',required=True, widget=forms.TextInput(
        attrs={'class': 'form-control mb-3','placeholder':'Location name'}))

    class Meta:
        model = Location
        fields = ('name',)
        

class ProductForm(forms.ModelForm):
    name = forms.CharField(label='',required=True, widget=forms.TextInput(
        attrs={'class': 'form-control mb-3','placeholder':'Product name'}))
    qty = forms.IntegerField(label='',widget=forms.TextInput(
        attrs={'class': 'form-control mb-3','placeholder':'Product quantity'}))

    class Meta:
        model = Product
        fields = ('name', 'qty',)


class UserForm(forms.ModelForm):
    name = forms.CharField(label='',required=True, widget=forms.TextInput(
        attrs={'class': 'form-control mb-3','placeholder':'User name'}))
    email = forms.CharField(label='',widget=forms.TextInput(
        attrs={'class': 'form-control mb-3','placeholder':'User email'}))

    class Meta:
        model = User
        fields = ('name', 'email',)


class MovementForm(forms.ModelForm):
    location_to = forms.ModelChoiceField(
        queryset=Location.objects.all(), empty_label="----Select Location----",
        widget=forms.Select(
            attrs={'class': 'form-control form-control-sm mb-3'}),
        required=True, label='Location'
    )

    class Meta:
        model = Movement
        fields = ('location_to',)


