from django.shortcuts import render
from apps.hello.models import Contact


def index(request):
    contacts = Contact.objects.first()
<<<<<<< HEAD
    return render(request, 'hello/hello.html', {'contacts': contacts})
=======
    return render(request, 'hello.html', {'contacts': contacts})
>>>>>>> t3_middleware
