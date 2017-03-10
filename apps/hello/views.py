from django.shortcuts import render
from apps.hello.models import Contact


def start_page(request):
    return render(request, 'start_page.html')
