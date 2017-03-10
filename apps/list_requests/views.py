from django.shortcuts import render

from list_requests.models import StoredRequests


def list_requests(request):
    selected_requests = StoredRequests.objects.order_by('-request_time')[:10]
    return render(
        request,
        'requests.html',
        {'selected_requests': selected_requests}
    )
