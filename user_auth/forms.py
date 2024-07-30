"""
Forms module for user authentication and registration.

This module contains form classes for user registration and authentication,
customized to include additional fields and Bootstrap styling.
"""

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class RegForm(UserCreationForm):
    """
    A form for creating new users. Inherits from UserCreationForm.
    
    Adds additional fields for email, first name, and last name, and applies Bootstrap 
    'form-control' class to all input fields for consistent styling.
    """
    
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control'}),
        help_text="Enter a valid email address."
    )
    first_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        help_text="Enter your first name."
    )
    last_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        help_text="Enter your last name."
    )
    
    class Meta:
        """
        Meta class to specify the model and fields that this form will interact with.
        """
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
    
    def __init__(self, *args, **kwargs):
        """
        Initialize the form by calling the parent constructor and then apply the 
        'form-control' class to the username, password1, and password2 fields to ensure 
        consistent Bootstrap styling.
        """
        super(RegForm, self).__init__(*args, **kwargs)
        
        # Add Bootstrap 'form-control' class to the username field
        self.fields['username'].widget.attrs['class'] = 'form-control'
        
        # Add Bootstrap 'form-control' class to the password1 field
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        
        # Add Bootstrap 'form-control' class to the password2 field
        self.fields['password2'].widget.attrs['class'] = 'form-control'


class CustomAuthenticationForm(AuthenticationForm):
    """
    A form for authenticating users. Inherits from AuthenticationForm.
    
    Applies Bootstrap 'form-control' class to username and password fields for consistent styling.
    """
    
    def __init__(self, *args, **kwargs):
        """
        Initialize the form by calling the parent constructor and then apply the 
        'form-control' class to the username and password fields to ensure consistent 
        Bootstrap styling.
        """
        super(CustomAuthenticationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['password'].widget.attrs.update({'class': 'form-control'})
