from django.shortcuts import render
from apps.hello.models import Contact


def index(request):
    contacts = Contact.objects.get(pk=1)
    return render(request, 'base.html', {'contacts': contacts})
