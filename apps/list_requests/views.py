from django.shortcuts import render


def list_requests(request):
    return render(request, "requests_page.html")
