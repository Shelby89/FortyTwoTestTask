from django.db import models
from django.dispatch import receiver
from django.db.models import signals
from django.contrib.auth.models import User


class Contact(models.Model):
    name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    date_of_birth = models.DateField("date of birth")
    bio = models.TextField()
    email = models.EmailField()
    jabber = models.CharField(max_length=30)
    skype = models.CharField(max_length=30)
    other_contacts = models.TextField()
