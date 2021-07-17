from django.urls import path
from .views import *

urlpatterns = [
    path('', Contact.as_view(), name='contact')
]
