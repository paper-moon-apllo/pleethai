from django.shortcuts import render
from django.views import View
from django.views.generic import FormView
from django.views.generic.base import TemplateView

from .forms import RequestForm


# for Request Screen
class MailInput(FormView):
    template_name = 'request.html'
    form_class = RequestForm
    success_url = 'mail/confirm/'

    def form_valid(self, form):
        return render(self.request, self.template_name, {'form': form})


def mail_confirm(request):
    return render(request, 'request_confirm.html')


def mail_complete(request):
    return render(request, 'request_complete.html')
