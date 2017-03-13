import json
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect
from django.forms import model_to_dict
from django.core.urlresolvers import reverse

from forms import EditForm
from apps.hello.models import Contact


def edit(request):
    obj = Contact.objects.first()
    form = EditForm(request.POST or None,
                             instance=obj)

    if request.is_ajax()  and request.method == 'POST':
        if form.is_valid():
            response_data = {}

            try:
                form.save()
                response_data['msg'] = u'Record was updated successfully'
            except:
                response_data['msg'] = u'Failed to update the record'

            return HttpResponse(json.dumps(response_data),
                            content_type="application/json")

        response_data = dict(form.errors)
        response_data['msg'] = u'You have errors in form fields'
        return HttpResponseBadRequest(json.dumps(response_data))

    return render(request, 'edit.html', {'form': form})
