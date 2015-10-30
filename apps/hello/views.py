from django.shortcuts import render
from apps.hello.models import Contact


def index(request):
    try:
        contacts = Contact.objects.first()
    except Contact.DoesNotExist:
        contacts = None

    return render(request, 'hello/hello.html', {'contacts': contacts})
