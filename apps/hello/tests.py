# -*- coding: utf-8 -*-
from django.test import TestCase
from django.core.urlresolvers import reverse
from apps.hello.models import Contact


class SomeTests(TestCase):

    fixtures = ['initial_data.json']

    def test_db_is_not_empty(self):
        "DB must not be empty"
        db_not_empty = Contact.objects.exists()
        self.assertEqual(db_not_empty,
                         True,
                         "DB is empty!")

    def test_db_many_rows(self):
        "DB must not have many rows"
        db_not_empty = Contact.objects.count()
        self.assertEqual(db_not_empty,
                         1,
                         "DB has %r rows!" % Contact.objects.count())

    def test_my_contact(self):
        "My contacts must be in DB"
        my_contact_en = Contact.objects.filter(name="Dmytro",
                                               last_name="Sapotnitskiy"
                                               ).count()
        my_contact_ru = Contact.objects.filter(name="Дмитрий",
                                               last_name="Сапотницкий"
                                               ).count()
        my_contact_ua = Contact.objects.filter(name="Дмитро",
                                               last_name="Сапотніцький"
                                               ).count()
        my_contact = my_contact_en + my_contact_ru + my_contact_ua
        self.assertEqual(my_contact, 1, "DB has not my contacts")

    def test_view_exist(self):
        "View must exist"
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_used_template(self):
        "hello.html must be used in response"
        response = self.client.get(reverse('index'))
        self.assertTemplateUsed(response, 'hello.html')

    def test_all_fields_exist(self):
        "All fields must be displayed"
        response = self.client.get(reverse('index'))
        contacts = Contact.objects.get(pk=1)
        self.assertContains(response, contacts.name)
        self.assertContains(response, contacts.last_name)
        birthday = contacts.date_of_birth.strftime("%B %d, %Y")
        self.assertContains(response, birthday)
        self.assertContains(response, contacts.bio[:3])
        self.assertContains(response, contacts.email)
        self.assertContains(response, contacts.jabber)
        self.assertContains(response, contacts.skype)
        self.assertContains(response, contacts.other_contacts[:3])

    def test_utf_8(self):
        "For correct display cyrrilic charset utf-8 is needed"
        response = self.client.get(reverse('index'))
        self.assertContains(response, 'utf-8')
