# -*- encoding: utf-8 -*-
import datetime
from django.test import TestCase
from django.core.urlresolvers import reverse

from ..forms import EditForm


class Ticket_5_Tests_Form(TestCase):

    def setUp(self):
        self.form = EditForm
        self.valid_form_data = {
            'name': 'Dmytro',
            'last_name': 'Sapotnitskiy',
            'date_of_birth': datetime.date(year=1989, month=3, day=24),
            'bio': 'Biography',
            'email': 'email@email.com',
            'jabber': 'jabber@jabber.com', 
            'skype': 'some_skype',
            'other_contacts': 'Here comes some other contacts',
        }

    def test_edit_form_with_no_data(self):
        """
        Test that EditForm can't be empty
        """
        self.assertFalse(self.form(data={}).is_valid())

    def test_edit_form_with_invalid_data(self):
        """
        Test that EditForm is invalid when invalid data is
        given
        """
        data = {'name': 'Dmytro', 'last_name': 'Sap'}
        self.assertFalse(self.form(data=data).is_valid())

    def test_edit_form_with_valid_data(self):
        """
        Test that EditForm is valid if sufficient data is
        given
        """
        data = self.valid_form_data
        self.assertTrue(self.form(data=data).is_valid())
