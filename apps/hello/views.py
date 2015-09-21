from django.shortcuts import render
from apps.hello.models import Contact


def index(request):
    try:
        contacts = Contact.objects.all()
    except Contact.DoesNotExist:
        contacts = None

    return render(request, 'hello.html', {'contacts': contacts})
