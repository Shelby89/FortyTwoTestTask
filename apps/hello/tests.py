# -*- coding: utf-8 -*-
from django.test import TestCase
from django.core.urlresolvers import reverse


class SomeTests(TestCase):

    fixtures = ['initial_data.json']

    def test_mockup(self):
        """
        Test mockup that return hard-coded data.
        """
        response = self.client.get(reverse('hello:start_page'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Dmytro")
        self.assertContains(response, "Sapotnitskiy")

    def test_view_exist(self):
        """
        View must exist
        """
        response = self.client.get(reverse('hello:index'))
        self.assertEqual(response.status_code, 200)

    def test_view_with_initial_data(self):
        """
        View must response with hard-coded data
        """
        response = self.client.get(reverse('hello:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Dmytro")
        self.assertContains(response, "Sapotnitskiy")
