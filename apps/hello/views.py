from django.shortcuts import render
from apps.hello.models import Contact


def index(request):
    contacts = Contact.objects.first()
    return render(request, 'hello/hello.html', {'contacts': contacts})
