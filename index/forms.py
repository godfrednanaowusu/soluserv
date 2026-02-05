from django.forms import ModelForm
from django import forms
from .models import Contact, CareerDetail, NewsLetter

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['full_name', 'email', 'subject', 'message']

class CareerDetailForm(ModelForm):
    class Meta:
        model = CareerDetail
        fields = ['first_name', 'last_name', 'email', 'phone', 'file', 'message']

class NewsLetterForm(forms.ModelForm):
    class Meta:
        model = NewsLetter
        fields = ['email']