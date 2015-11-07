from django.test import TestCase
from hello.models import Contact


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
        my_contact = Contact.objects.filter(name="Dmytro",
                                            last_name="Sapotnitskiy").count()
        self.assertEqual(my_contact, 1, "DB has not my contacts")
