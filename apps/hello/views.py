from django.shortcuts import render


def start_page(request):
    return render(request, 'start_page.html')


def index(request):
    return render(request, 'start_page.html')
