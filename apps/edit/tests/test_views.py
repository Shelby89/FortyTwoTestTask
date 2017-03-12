# -*- encoding: utf-8 -*-
import datetime
from django.test import TestCase, RequestFactory
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from .. forms import EditForm
from .. views import edit
from apps.hello.models import Contact


class Ticket_5_Tests_View(TestCase):
    def test_mockup(self):
        """
        Mockup of edit page should contain <form> tag and
        based on edit_page.html
        """
        response = self.client.get(reverse('edit:edit_page'))
        self.assertTemplateUsed(response, 'edit_page.html')
        self.assertContains(response, "form")

    def test_view_with_models_data(self):
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

    def test_view_with_models_data(self):
        """
        View must response with hard-coded data
        """
        response = self.client.get(reverse('edit:edit'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "form")
        self.assertContains(response, "Dmytro")
        self.assertContains(response, "Sapotnitskiy")

class Ticket_5_Tests_Edit_Form(TestCase):

    fixtures = ['initial_data.json']

    """
    A test case for a view `HelloEditView`
    """
    def setUp(self):
        self.user = User.objects.create_user(username='test', password='pass')
        self.form = EditForm
        self.valid_form_data = {
            'name': 'Dmy',
            'last_name': 'Sapotnitskiy',
            'date_of_birth': datetime.date(year=1989, month=3, day=24),
            'bio': 'Biography',
            'email': 'email@email.com',
            'jabber': 'jabber@jabber.com', 
            'skype': 'some_skype',
            'other_contacts': 'Here comes some other contacts',
        }

    def test_edit_view_template(self):
        """
        Test that EditView return appropriate template
        """
        response = self.client.get(reverse("edit:edit"))

        self.assertTemplateUsed(response, 'edit.html')
        self.assertEqual(response.status_code, 200)

    def test_edit_change_by_valid_data(self):
        """
        Test that data can be changed by EditView with valid data
        """
        before = Contact.objects.first()
        response = self.client.get(reverse("edit:edit"))
        data = self.valid_form_data
        response = self.client.post(
            reverse("edit:edit"),
            data
        )
        self.assertEqual(response.status_code, 302)
        after = Contact.objects.first()
        self.assertNotEqual(before.name, after.name)

    def test_edit_change_by_invalid_data(self):
        """
        Test that data can't be changed by EditView with valid data
        """
        before = Contact.objects.first()
        response = self.client.get(reverse("edit:edit"))
        data = self.valid_form_data
        response = self.client.post(
            reverse("edit:edit"),
            {'name': 'Dmytro', 'last_name': 'Sapotnitskiy', 'email': ''}
        )
        # self.assertEqual(response.status_code, 200)
        after = Contact.objects.first()
        self.assertEqual(before.name, after.name)
