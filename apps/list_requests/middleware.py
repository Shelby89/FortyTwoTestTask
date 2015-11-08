from list_requests.models import StoredRequests


class MyHttpRequestMiddleware(object):
    def process_request(self, request):
        if request.is_ajax() is not True:
            try:
                req = StoredRequests()
                req.method = request.META.get('REQUEST_METHOD')
                req.path_info = request.META.get('PATH_INFO')
                req.server_protocol = request.META.get('SERVER_PROTOCOL')
                req.server_port = request.META.get('SERVER_PORT')
                req.remote_address = request.META.get('REMOTE_ADDR')
                req.save()
            except KeyError:
                pass
        return None
