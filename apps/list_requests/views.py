import json
from django.shortcuts import render, HttpResponse
from django.template.loader import render_to_string
from datetime import datetime, timedelta

from list_requests.models import StoredRequests


def list_requests(request):
    status = request.GET.get('status', 'focused')
    if status == "focused":
        StoredRequests.objects.filter(viewed=False).update(viewed=True)
    selected_requests = StoredRequests.objects.order_by('-request_time')[:10]
    return render(
        request,
        'requests.html', 
        {'selected_requests': selected_requests}
    )

def table(request):
    requests = StoredRequests.objects.order_by('-request_time')[:10]
    data = dict(
        count=StoredRequests.objects.filter(viewed=False).count(),
        text=render_to_string('table.html', dict(requests=requests))
    )
    return HttpResponse(json.dumps(data), content_type='application/json')
