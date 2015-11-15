from django.utils import timezone
from django.shortcuts import render
from list_requests.models import StoredRequests

time_per_session1 = []


def list_requests(request):
    if request.is_ajax() is False and request.method == 'GET':
        time_per_session1.append(StoredRequests.objects.last().request_time)
    
    if len(time_per_session1) == 0:
        time_per_session = None
        
    else:
        time_per_session = time_per_session1[-1]

    selected_requests = StoredRequests.objects.order_by('-request_time')[:10]
    count_req = StoredRequests.objects.filter(request_time__gt=time_per_session).count
    
    
    
    return render(
        request,
        'requests.html',
        {
            'selected_requests': selected_requests,
            'count_req': count_req,
            'time_per_session': time_per_session
        },
    )
