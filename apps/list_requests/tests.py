# -*- encoding: utf-8 -*-
from django.test import TestCase
from django.core.urlresolvers import reverse
import time

from apps.list_requests.models import StoredRequests


class Ticket_3_Tests(TestCase):
    def test_check_url_requests_added(self):
        "url /requests must be in hello.html"
        response = self.client.get(reverse('hello:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "<a href='/requests/'>requests")
    
    def test_used_template_for_requests(self):
        "requests.html must be used in response"
        response = self.client.get(reverse('list_requests:requests'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'requests.html')
    
    def test_middleware_is_working_and_return_my_request(self):
        "Check if middleware is working and return new request"
        response = self.client.get(reverse('list_requests:requests'))
        self.assertEqual(response.status_code, 200)
        content = response.content
        first_td = content.find("<td>")
        last_td = content.find("</td>")
        last1 = content[first_td:last_td]
        time.sleep(1)
        response = self.client.get(reverse('list_requests:requests'))
        content = response.content
        first_td = content.find("<td>")
        last_td = content.find("</td>")
        last2 = content[first_td:last_td]
        self.assertNotEqual(last1, last2)

    def test_middleware_doesnt_save_ajax_requests(self):
        "Middleware must not save ajax requests and requests for staticfiles"
        StoredRequests.objects.all().delete()
        self.client.get(reverse('list_requests:requests'),
                        HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        requests = StoredRequests.objects.all().count()
        self.assertEquals(requests, 0)
        static_files_req = StoredRequests.objects.filter(
            path_info__contains='static'
            ).count()
        self.assertEquals(static_files_req, 0)

    def test_requests_page_return_ten_requests(self):
        "View must return no more than 10 requests"
        for i in range(0, 15):
            response = self.client.get(reverse('list_requests:requests'))
            self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['selected_requests'].count(), 10)
        
    