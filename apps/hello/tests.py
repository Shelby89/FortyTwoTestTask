from django.test import TestCase

# Create your tests here.


class SomeTests(TestCase):
    #def test_math(self):
    #    "Here goes testing of math function"
    #    assert(2 + 2 == 5)
	def TestMyContact(self):
		# Primary key must be "1" for my contact
		my_contact = Contact.object.get(pk=1)
		self.assertEqual(my_contact.last_name, "Sapotnitskiy", "Its not my contacts!")
