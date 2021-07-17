from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import *

# Create your views here.

class Contact(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = '/'

    def form_valid(self, form):
        form.save_msg()
        return super().form_valid(form)
