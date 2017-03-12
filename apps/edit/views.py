from django.shortcuts import render, HttpResponseRedirect
from django.forms import model_to_dict
from django.core.urlresolvers import reverse

from forms import EditForm
from apps.hello.models import Contact


def edit(request):
    if request.method == 'POST':
        form = EditForm(request.POST, instance=Contact.objects.first())
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('edit:edit'))
    else:
        data = model_to_dict(Contact.objects.first())
        form = EditForm(data)

    return render(request, 'edit.html', {'form': form})