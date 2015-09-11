from django.conf import settings
from django.contrib.auth import models as auth_models
from django.contrib.auth.management import create_superuser
from django.db.models import signals
from django.db import models
from django.contrib.auth.models import User

signals.post_syncdb.disconnect(
    create_superuser,
    sender=auth_models,
    dispatch_uid='django.contrib.auth.management.create_superuser')


def create_testuser(app, created_models, verbosity, **kwargs):
    if not settings.DEBUG:
        return
    try:
        auth_models.User.objects.get(username='admin')
    except auth_models.User.DoesNotExist:
        print '*' * 80
        print 'Creating test user -- login: admin, password: admin'
        print '*' * 80
        assert auth_models.User.objects.create_superuser('admin',
                                                         'shelby_dima@mail.ru',
                                                         'admin')
    else:
        print 'Admin user already exists.'

signals.post_syncdb.connect(
    create_testuser,
    sender=auth_models,
    dispatch_uid='common.models.create_testuser')


class Contact(models.Model):
    name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    date_of_birth = models.DateField('date of birth')
    bio = models.TextField()
    email = models.EmailField()
    jabber = models.CharField(max_length=30)
    skype = models.CharField(max_length=30)
    other_contacts = models.TextField()
