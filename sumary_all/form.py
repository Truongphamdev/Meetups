from django import forms
from .models import Participant,Meetup


class Registration(forms.Form):
    email = forms.EmailField()
