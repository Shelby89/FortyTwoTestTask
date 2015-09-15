from django.shortcuts import render
from apps.hello.models import Contact


def index(request):
    try:
        contacts = Contact.objects.get(pk=1)
    except Contact.DoesNotExist:
        contacts = None

    return render(request, 'hello.html', {'contacts': contacts})
