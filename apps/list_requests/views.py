from django.shortcuts import render
from datetime import datetime, timedelta

from list_requests.models import StoredRequests

time_per_session = None
status = ""

def list_requests(request):
    global status, time_per_session
    
    if request.is_ajax() is True and request.method == 'GET':
        if request.GET.get('status') == "blurred":
            status = "blurred"
        elif request.GET.get('status') == "focused":
            status = "focused"
    
    if status == "blurred":
        if request.GET.get('last_req') is not None:
            date_object = datetime.strptime(
                request.GET.get('last_req'),
                '%d/%b/%Y %H:%M:%S'
            )
            time_per_session = date_object + timedelta(seconds=1)
        count_req = StoredRequests.objects.filter(
            request_time__gt=time_per_session
        ).count()
    else:
        count_req = 0

    selected_requests = StoredRequests.objects.order_by('-request_time')[:10]

    return render(
        request,
        'requests.html',
        {
            'selected_requests': selected_requests,
            'count_req': count_req,
        },
    )
