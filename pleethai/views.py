from django.shortcuts import render


# for Request Screen
def mail_input(request):
    return render(request, 'request.html')


def mail_confirm(request):
    return render(request, 'request_confirm.html')


def mail_complete(request):
    return render(request, 'request_complete.html')
