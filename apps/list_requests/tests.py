# -*- encoding: utf-8 -*-
from django.test import TestCase
from django.core.urlresolvers import reverse


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
