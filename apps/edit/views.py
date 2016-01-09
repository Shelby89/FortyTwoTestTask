from django.shortcuts import render


def edit(request):
    return render(request, 'edit.html')
