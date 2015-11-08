from django.db import models


class StoredRequests(models.Model):
    request_time = models.DateTimeField(auto_now_add=True)
    method = models.CharField(max_length=5)
    path_info = models.CharField(max_length=200)
    server_protocol = models.CharField(max_length=50)
    server_port = models.IntegerField()
    remote_address = models.CharField(max_length=50)
