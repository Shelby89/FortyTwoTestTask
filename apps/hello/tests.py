from django.test import TestCase
from .models import Contact

# Create your tests here.


class SomeTests(TestCase):
    #def test_math(self):
    #    "Here goes testing of math function"
    #    assert(2 + 2 == 5)
	def test_my_contact(self):
		" Primary key must be "1" for my contact"
		my_contact = Contact.objects.get(pk = 1)
		my_last_name = my_contact.last_name
		self.assertEqual(my_last_name, "Sapotnitskiy", "Its not my contacts!")
