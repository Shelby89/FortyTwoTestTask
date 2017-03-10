from list_requests.models import StoredRequests


class MyHttpRequestMiddleware(object):
    def process_request(self, request):
        if request.is_ajax() or 'static' in request.META.get('PATH_INFO'):
            return

        StoredRequests(
            method=request.META.get('REQUEST_METHOD'),
            path_info=request.META.get('PATH_INFO'),
            server_protocol=request.META.get('SERVER_PROTOCOL'),
            server_port=request.META.get('SERVER_PORT'),
            remote_address=request.META.get('REMOTE_ADDR')
        ).save()