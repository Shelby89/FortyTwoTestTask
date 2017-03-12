# -*- encoding: utf-8 -*-
from django.test import TestCase
from django.core.urlresolvers import reverse
import time

from apps.list_requests.models import StoredRequests


class Ticket_5_Tests(TestCase):
    def test_mockup(self):
        """
        Mockup of edit page should contain <form> tag and
        based on edit_page.html
        """
        response = self.client.get(reverse('edit:edit_page'))
        self.assertTemplateUsed(response, 'edit_page.html')
        self.assertContains(response, "form")

    def test_view_with_hardcoded_data(self):
        """
        View must response with hard-coded data
        """
        response = self.client.get(reverse('edit:edit'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "form")
        self.assertContains(response, "Dmytro")
        self.assertContains(response, "Sapotnitskiy")

    def test_view_used_template(self):
        """
        Test that view for index page return template hello.html in response
        """
        response = self.client.get(reverse('edit:edit'))
        self.assertTemplateUsed(response, 'edit.html')