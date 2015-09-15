# -*- coding: utf-8 -*-
from django.test import TestCase
from .models import Contact


class SomeTests(TestCase):
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
