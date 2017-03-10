# -*- encoding: utf-8 -*-
from django.test import TestCase
from django.core.urlresolvers import reverse

from apps.list_requests.models import StoredRequests


class Ticket_3_Tests(TestCase):
    def test_mockup(self):
        """
        Test that mockup of page with requests exists.
        """
        response = self.client.get(reverse('hello:requests_page'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, reverse('hello:start_page'))

    def test_view_exist_with_initial_data(self):
        """
        View must response with hard-coded data
        """
        response = self.client.get(reverse('list_requests:requests'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "05/Jan/2016 21:50:10")
        self.assertContains(response, "GET")
        self.assertContains(response, "/requests/")
        self.assertContains(response, "HTTP/1.1")
        self.assertContains(response, "10.240.0.53:8080")
        self.assertContains(response, "True")

    def test_view_used_template(self):
        """
        Test that view for page with requests return
        template requests_page.html
        """
        response = self.client.get(reverse('list_requests:requests'))
        self.assertTemplateUsed(response, 'requests_page.html')

    def test_model_exist_with_no_data(self):
        """
        Test that model exists in DB
        """
        data_in_model = StoredRequests.objects.all().count()
        self.assertEqual(data_in_model, 0)

    def test_model_can_store_data(self):
        """
        Test that model can store new data
        """
        StoredRequests.objects.create(
            method="GET",
            path_info="some_url/",
            server_protocol="HTTP/1.1",
            server_port="8000",
            remote_address="1.1.1.1"
        )
        data_in_model = StoredRequests.objects.all()
        self.assertEqual(data_in_model.count(), 1)

        row = data_in_model.get(id=1)
        self.assertEqual(row.remote_address, "1.1.1.1")
        self.assertNotEqual(row.request_time, None)
        self.assertEqual(row.viewed, False)
