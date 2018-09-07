from django.contrib.auth.models import User
from django import forms
from website.models import *

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'first_name', 'last_name',)

# class ProfileForm(forms.ModelForm):

#     class Meta:
#         model = Profile
#         fields = ('rank', 'team', 'role')

class DetaineeForm(forms.ModelForm):
    
    class Meta:
        model = Detainee
        fields = ('name', 'alias', 'date_captured', 'capture_location', 'team')


class SessionForm(forms.ModelForm):

    class Meta:
        model = Session
        fields= ('name', 'role', 'length_of_sess', 'detainee')


class ReportForm(forms.ModelForm):

    class Meta:
        model = Report
        fields= ('creator', 'name', 'detainee', 'date_due', 'text_data')

class Updatesession(forms.ModelForm):

    class Meta:
        model = Session
        fields = ('role',)


