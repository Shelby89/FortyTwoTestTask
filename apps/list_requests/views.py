import datetime

from django.utils import timezone
from django.shortcuts import render
from list_requests.models import StoredRequests
from django.http import HttpResponse

time_per_session1 = []

def list_requests(request):
    print time_per_session1
    if request.is_ajax() == False and request.method == 'GET':
        data = timezone.now()
    else:
        data = None
        
    if data != None:
            time_per_session1.append(data)
    
    time_per_session = time_per_session1[-1] 
    print "Time per session %s" % time_per_session
    print "IS_AJAX = %s" % request.is_ajax()
    print "REQUEST METHOD = %s" % request.method
    print "============================"
    # print "Time of last req %s" % StoredRequests.objects.last().request_time
    #print StoredRequests.objects.last().request_time <= time_per_session
    selected_requests = StoredRequests.objects.filter(request_time__gte=time_per_session).order_by('-request_time')[:10]
    #selected_requests = StoredRequests.objects.order_by('-request_time')[:10]
    count_req = StoredRequests.objects.filter(request_time__gte=time_per_session).count
    return render(request,
                    'list_requests/requests.html',
                        {'selected_requests': selected_requests,
                        'count_req': count_req,
                        'time_per_session': time_per_session},
                    )
