# -*- coding: utf-8 -*-
from django.test import TestCase
from django.core.urlresolvers import reverse
from apps.hello.models import Contact


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
        View must response with initial data
        """
        response = self.client.get(reverse('hello:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Dmytro")
        self.assertContains(response, "Sapotnitskiy")

    def test_view_used_template(self):
        """
        Test that view for index page return template hello.html in response
        """
        response = self.client.get(reverse('hello:index'))
        self.assertTemplateUsed(response, 'hello.html')

    def test_view_with_no_data(self):
        """
        Test if there are 0 rows in DB
        """
        Contact.objects.all().delete()
        response = self.client.get(reverse('hello:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "There is no information")
        self.assertEqual(response.context['contacts'], None)

    def test_view_if_two_rows_in_db(self):
        """
        Test that view shows only firts row from DB
        """
        Contact.objects.create(name="Test",
                               last_name="Test",
                               date_of_birth="1989-03-24"
                               )
        response = self.client.get(reverse('hello:index'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['contacts'],
                         Contact.objects.first())
        self.assertEqual(response.context['contacts'].name, "Dmytro")
        self.assertEqual(response.context['contacts'].last_name,
                         "Sapotnitskiy")
        self.assertContains(response, "Dmytro")
        self.assertContains(response, "Sapotnitskiy")

    def test_model_exist_with_no_data(self):
        """
        Test that model exists in DB
        """
        Contact.objects.all().delete()  # because test created with init. data
        data_in_model = Contact.objects.all()
        self.assertEqual(len(data_in_model), 0)

    def test_model_can_store_data(self):
        """
        Test that model can store new data
        """
        Contact.objects.create(name="Test",
                               last_name="Test",
                               date_of_birth="1989-03-24"
                               )
        data_in_model = Contact.objects.all().count()
        self.assertEqual(data_in_model, 2)

    def test_all_fields_exist(self):
        "All fields must be displayed"
        response = self.client.get(reverse('hello:index'))
        contacts = Contact.objects.first()
        self.assertContains(response, contacts.name)
        self.assertContains(response, contacts.last_name)
        birthday = contacts.date_of_birth.strftime("%B %d, %Y")
        self.assertContains(response, birthday)
        self.assertContains(response, contacts.bio[:3])
        self.assertContains(response, contacts.email)
        self.assertContains(response, contacts.jabber)
        self.assertContains(response, contacts.skype)
        self.assertContains(response, contacts.other_contacts[:3])

    def test_check_cyrillic(self):
        "Test for correct display of cyrillic"
        contacts = Contact.objects.first()
        contacts.name = "Дмитро"
        contacts.last_name = "Сапотніцький"
        contacts.save()
        response = self.client.get(reverse('hello:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'utf-8')
        name_cyrillic = u'Дмитро'
        last_name_cyrillic = u'Сапотніцький'
        self.assertContains(response, name_cyrillic)
        self.assertContains(response, last_name_cyrillic)
