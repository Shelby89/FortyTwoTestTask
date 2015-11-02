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
    time_per_session = timezone.now()
    #print time_1
    #print StoredRequests.objects.last().request_time
    #print StoredRequests.objects.last().request_time <= time_per_session
    #selected_requests = StoredRequests.objects.filter(request_time__lte=time_per_session).order_by('-request_time')[:10]
    selected_requests = StoredRequests.objects.order_by('-request_time')[:10]
    count_req = StoredRequests.objects.all().count
    return render(request,
                    'list_requests/requests.html',
                        {'selected_requests': selected_requests,
                        'count_req': count_req,
                        'time_per_session': time_per_session},
                    )