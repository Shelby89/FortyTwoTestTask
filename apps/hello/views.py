from django.shortcuts import render
from apps.hello.models import Contact


def index(request):
    try:
        contacts = Contact.objects.get(name="Dmytro",
                                       last_name="Sapotnitskiy")
    except Contact.DoesNotExist:
        contacts = None

    return render(request, 'hello.html', {'contacts': contacts})
