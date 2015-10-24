import datetime

from django.utils import timezone
from django.shortcuts import render
from list_requests.models import StoredRequests

def list_requests(request):
    # print datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # print request.META.get('PATH_INFO')
    # print request.META.get('REQUEST_METHOD')
    # print request.META.get('SERVER_PROTOCOL')
    # print '%s  %s', request.META.get('REMOTE_ADDR'), request.META.get('SERVER_PORT')
    # print "====================="
    # print request.META.get ('HTTP_X_FORWARDED_FOR')
    selected_requests = StoredRequests.objects.order_by('-request_time')[:10]
    return render(request, 'list_requests/requests.html', {'selected_requests': selected_requests})