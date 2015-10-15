from django.db import models
from random import randint
from django.utils.text import slugify
from datetime import date

class Event(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateField()
    nameyear = models.CharField(max_length=204)

    def create_nameyear(self):
        return slugify(self.name + "-" + str(self.date.year))

class Contact(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    full_name = models.CharField(max_length=60,default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    event_met = models.ForeignKey(Event)
    endpoint = models.TextField(unique=True,max_length=66)
    is_favorite = models.BooleanField(default=False)
    email = models.EmailField(max_length=254,unique=True)
    phone = models.BigIntegerField(unique=True)

    def get_full_name(self):
        return self.first_name + " " + self.last_name

    def create_endpoint(self):
        phonestr = str(self.phone)
        return slugify(self.first_name + self.last_name + str(phonestr[len(phonestr)-4:len(phonestr):1]))
