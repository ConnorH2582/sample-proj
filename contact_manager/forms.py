from django.forms import ModelForm
from contact_manager.models import Contact, Event
from django import forms

class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'date']
        widgets = {
        'name':forms.TextInput(attrs={'placeholder':'Event name'}),
        'date':forms.DateInput(attrs={'placeholder':'Event date (mm/dd/yyyy)'}),
        }

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['first_name','last_name','is_favorite','email','phone']
        widgets = {
        'first_name':forms.TextInput(attrs={'placeholder':'First name '}),
        'last_name':forms.TextInput(attrs={'placeholder':'Last name'}),
        'is_favorite':forms.CheckboxInput(attrs={'label':'Add as favorite'}),
        'email':forms.EmailInput(attrs={'placeholder':'Contact email'}),
        'phone':forms.NumberInput(attrs={'placeholder':'Phone number'}),
        }
