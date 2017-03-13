from django import forms
from django.utils.safestring import mark_safe
from django.contrib.staticfiles.storage import staticfiles_storage


class DatePickerWidget(forms.TextInput):
    class Media:
        css = {
            'all': (
                staticfiles_storage.url('css/jquery-ui.css'),
                staticfiles_storage.url('css/jquery-ui.structure.css'),
                staticfiles_storage.url('css/jquery-ui.theme.css'),
            )
        }

        js = (
            staticfiles_storage.url('jquery/jquery-ui.js'),
        )

    def render(self, name, value, attrs=None):
        html = super(DatePickerWidget, self).render(name, value, attrs)
        html += mark_safe('<script>'
                          'document.addEventListener("DOMContentLoaded",'
                          'function () {$("#id_%s").datepicker();})'
                          '</script>' % name)
        return html