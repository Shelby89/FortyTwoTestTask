# -*- encoding: utf-8 -*-
from django.test import TestCase
from django.core.urlresolvers import reverse
import time

from apps.list_requests.models import StoredRequests


class Ticket_5_Tests(TestCase):
    def test_view_exist_for_edit_page(self):
        "url edit/ must contain <form> tag"
        response = self.client.get(reverse('edit:edit'))
        self.assertContains(response, "form")
