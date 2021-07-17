from django import forms
from django.forms.widgets import Textarea
from contact.models import *


class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)

    def save_msg(self):
        msg = Contact(name=self.cleaned_data['name'],email=self.cleaned_data['email'],message=self.cleaned_data['message'])
        msg.save()   
