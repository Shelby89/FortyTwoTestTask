import datetime

from django.utils import timezone
from django.shortcuts import render

def list_requests(request):
    print datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print request.META.get('PATH_INFO')
    print request.META.get('SERVER_PROTOCOL')
    print request.META.get('REQUEST_METHOD')
    #print request
    #print request.status_code
    print "====================="
    # print request.META
    return render(request, 'list_requests/requests.html')