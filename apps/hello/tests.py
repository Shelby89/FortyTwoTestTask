# -*- coding: utf-8 -*-
from django.test import TestCase
from django.core.urlresolvers import reverse


class SomeTests(TestCase):

    fixtures = ['initial_data.json']

    def test_no_rows_in_db(self):
        """
        Test mockup that return hard-coded data.
        """
        response = self.client.get(reverse('hello:start_page'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Dmytro")
        self.assertContains(response, "Sapotnitskiy")
