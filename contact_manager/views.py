from django.shortcuts import render,redirect
from django.views.generic import View
from contact_manager.forms import EventForm,ContactForm
from django import forms
from contact_manager.models import Contact, Event
import os
import requests
from datetime import date, datetime
from django.contrib.messages import error


class IndexView(View):
    template = 'contact_manager/index.html'

    def get(self, request):
        all_contacts = Contact.objects.all()
        all_events = Event.objects.all()
        return render(request, self.template,{'all_contacts':all_contacts,'all_events':all_events,})

class CreateEventView(View):
    template = 'contact_manager/create_event.html'

    def get(self, request):
        event_form = EventForm()
        return render(request, self.template, {'event_form':event_form})

    def post(self, request):
        submitted_form = EventForm(request.POST)
        if submitted_form.is_valid():
            submitted_name = submitted_form.cleaned_data.get('name')
            submitted_date = submitted_form.cleaned_data.get('date')
            new_event = Event(name=submitted_name, date=submitted_date)
            new_event.nameyear = new_event.create_nameyear()
            new_event.save()
            return redirect('contact_manager:index')
        error(request, 'Field missing or field error, please try again.')
        return redirect('contact_manager:create_event')

class EventProfileView(View):
    template = 'contact_manager/event_profile.html'

    def get(self, request, nameyear):
        viewed_event = Event.objects.filter(nameyear=nameyear)[0]
        event_month = viewed_event.date.strftime("%B")
        event_contacts = Contact.objects.filter(event_met=viewed_event)
        return render(request, self.template, {'viewed_event':viewed_event, 'event_month':event_month,'event_contacts':event_contacts})

class CreateContactView(View):
    template = 'contact_manager/create_contact.html'

    def get(self, request, nameyear):
        contact_event = Event.objects.filter(nameyear=nameyear)[0]
        contact_form = ContactForm()
        return render(request, self.template, {'contact_form':contact_form, 'contact_event':contact_event})

    def post(self, request, nameyear):
        contact_event = Event.objects.filter(nameyear=nameyear)[0]
        submitted_contact_form = ContactForm(request.POST)
        print(request.POST.get('is_favorite'))
        print(submitted_contact_form.is_valid())
        if submitted_contact_form.is_valid():
            submitted_first_name = submitted_contact_form.cleaned_data.get('first_name')
            submitted_last_name = submitted_contact_form.cleaned_data.get('last_name')
            submitted_email = submitted_contact_form.cleaned_data.get('email')
            submitted_phone = submitted_contact_form.cleaned_data.get('phone')
            submitted_full_name = submitted_first_name + " " + submitted_last_name
            new_contact = Contact(event_met=contact_event, first_name=submitted_first_name, last_name=submitted_last_name,full_name = submitted_full_name, email=submitted_email, phone=submitted_phone)
            new_contact.endpoint = new_contact.create_endpoint()
            if request.POST.get('is_favorite'):
                new_contact.is_favorite = True
            new_contact.save()
            return redirect('contact_manager:index')
        error(request, 'Field missing or field error, please try again.')
        return redirect('contact_manager:create_contact', nameyear=nameyear)

class ContactProfileView(View):
        template = 'contact_manager/contact_profile.html'

        def get(self, request, endpoint):
            viewed_contact = Contact.objects.filter(endpoint=endpoint)[0]
            contact_form = ContactForm()
            return render(request, self.template, {'contact_form':contact_form, 'viewed_contact':viewed_contact})

        def post(self, request, endpoint):
            viewed_contact = Contact.objects.filter(endpoint=endpoint)[0]
            if request.POST.get('update_contact') == 'Add Favorite':
                viewed_contact.is_favorite = True
            else:
                viewed_contact.is_favorite = False
            viewed_contact.save()
            return redirect('contact_manager:contact_profile', endpoint=endpoint)

class ContactSearchView(View):
    template = 'contact_manager/search_results.html'

    def get(self,request):
        if request.GET.get('search_query'):
            submitted_query = request.GET.get('search_query')
            search_matches = []
            if Contact.objects.filter(first_name__icontains=submitted_query):
                first_name_matches = Contact.objects.filter(first_name__icontains=submitted_query)
                search_matches += first_name_matches
            if Contact.objects.filter(last_name__icontains=submitted_query):
                last_name_matches = Contact.objects.filter(last_name__icontains=submitted_query)
                search_matches += last_name_matches
            if Contact.objects.filter(full_name__icontains=submitted_query):
                full_name_matches = Contact.objects.filter(full_name__icontains=submitted_query)
                search_matches += full_name_matches
            return render(request, self.template, {'search_matches':search_matches,'submitted_query':submitted_query})
        return redirect('contact_manager:index')
