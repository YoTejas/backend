from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import ReadOnlyPasswordHashField

class UserForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'is_active']
    
    def clean_password(self):
        return self.initial["password"]
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = user.email
        if commit:
            user.save()
        return user
    
class CustomUserForm(forms.ModelForm):

    password = ReadOnlyPasswordHashField(label="Password", help_text=(
        "Raw passwords are not stored, so there is no way to see "
        "this user's password, but you can change the password "
        "using <a href=\"../password/\">this form</a>."
    ))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'is_active', 'is_staff', 'is_superuser']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        self.cleaned_data['username'] = email  # Ensure username matches email
        return email
    
    def clean_password(self):
        return self.initial["password"]
