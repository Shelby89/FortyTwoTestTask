from django.test import TestCase
from apps.edit.widgets import DatePickerWidget


class Ticket_5_Tests_Widget(TestCase):
    def test_edit_form_with_rendered_widget(self):
        """
        Test that datepicker was added to TextInput field
        """
        widget = DatePickerWidget()
        html = widget.render(name='date', value='test')
        self.assertIn('name="date"', html)
        self.assertIn('$("#id_date")', html)