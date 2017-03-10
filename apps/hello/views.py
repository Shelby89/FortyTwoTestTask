from django.shortcuts import render
from apps.hello.models import Contact


def start_page(request):
    return render(request, 'start_page.html')


def index(request):
    contacts = Contact.objects.first()
    return render(request, 'hello.html', {'contacts': contacts})
