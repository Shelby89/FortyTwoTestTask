from django.test import TestCase
from django.core.urlresolvers import reverse


class SomeTests(TestCase):
    
    def test_used_template(self):
        "hello.html must be used in response"
        response = self.client.get(reverse('list_requests:requests'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'requests.html')