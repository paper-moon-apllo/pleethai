from django.conf import settings
from django.shortcuts import render
from django.views import View
from django.views.generic import FormView
from django.core.mail import send_mail
from django.template.loader import render_to_string

from .forms import RequestForm


# for Request Screen
class MailInput(FormView):
    template_name = 'request.html'
    form_class = RequestForm
    success_url = 'mail/confirm/'

    def form_valid(self, form):
        return render(self.request, self.template_name, {'form': form})


class MailConfirm(FormView):
    template_name = 'request_confirm.html'
    back_template_name = 'request.html'
    form_class = RequestForm
    success_url = 'mail/complete/'

    def form_valid(self, form):
        '''
        This method is called when valid form data has been POSTed from request input.
        '''
        return render(self.request, self.template_name, {'form': form})

    def form_invalid(self, form):
        '''
        This method is called when invalid form data has been POSTed from request input.
        '''
        return render(self.request, self.back_template_name, {'form': form})


class MailComplete(FormView):
    template_name = 'request_complete.html'
    form_class = RequestForm

    def form_valid(self, form):
        '''
        This method is called when valid form data has been POSTed from request confirm.
        '''

        context = {
            "form": form,
        }
        request_mail_send(context)

        return render(self.request, self.template_name, {'form': form})


def request_mail_send(context):
    subject = settings.REQUSET_MAIL_SEND_INFO.get('subject')
    message = render_to_string(
        settings.REQUSET_MAIL_SEND_INFO.get('templete_path'), context)
    from_email = settings.REQUSET_MAIL_SEND_INFO.get('from_email')
    recipient_list = settings.REQUSET_MAIL_SEND_INFO.get('recipient_list')
    send_mail(subject, message, from_email, recipient_list)
