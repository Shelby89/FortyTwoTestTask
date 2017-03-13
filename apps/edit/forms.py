from django import forms
from apps.hello.models import Contact
from widgets import DatePickerWidget


class EditForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'last_name', 'date_of_birth', 'bio', 'email', 'jabber', 'skype',
                  'other_contacts')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'date_of_birth': DatePickerWidget(attrs={'class': 'form-control'}),
            'bio': forms.Textarea(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'jabber': forms.EmailInput(attrs={'class': 'form-control'}),
            'skype': forms.TextInput(attrs={'class': 'form-control'}),
            'other_contacts': forms.Textarea(attrs={'class': 'form-control'})
        }
