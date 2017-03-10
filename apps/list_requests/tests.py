# -*- encoding: utf-8 -*-
from django.test import TestCase
from django.core.urlresolvers import reverse


class Ticket_3_Tests(TestCase):
    def test_mockup(self):
        "url /requests must be in hello.html"
        response = self.client.get(reverse('hello:requests_page'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, reverse('hello:start_page'))
