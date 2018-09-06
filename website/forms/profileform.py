from django.contrib.auth.models import User
from .models import Order, PaymentType
# from .models import Customer
from django import forms
from website.models import Profile



class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('rank', 'team', 'role')


