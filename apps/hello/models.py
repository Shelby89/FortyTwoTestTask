from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    date_of_birth = models.DateField("date of birth")
    bio = models.TextField()
    email = models.EmailField()
    jabber = models.CharField(max_length=30)
    skype = models.CharField(max_length=30)
    other_contacts = models.TextField()

    def __unicode__(self):
        full_name = self.last_name + " " + self.name
        return full_name
