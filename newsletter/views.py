from django.shortcuts import render, redirect
from .models import Newsletter
from .forms import NewsletterForm, SendMessageForm
from django.contrib import messages
from django.core.mail import send_mail
from django_pandas.io import read_frame


def newsletter(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Subscription Successful')
            return redirect('/')
    else:
        form = NewsletterForm()
    context = {
        'form': form,
    }
    return render(request, 'newsletter/newsletter.html', context)


def send_message(request):
    emails = Newsletter.objects.all()
    df = read_frame(emails, fieldnames=['email'])
    mail_list = df['email'].values.tolist()
    print(mail_list)
    if request.method == 'POST':
        form = SendMessageForm(request.POST)
        if form.is_valid():
            form.save()
            title = form.cleaned_data.get('title')
            message = form.cleaned_data.get('message')
            send_mail(
                title,
                message,
                '',
                mail_list,
                fail_silently=False,
            )
            messages.success(request, 'Message has been sent to the Mail List')
            return redirect('send_message')
    else:
        form = SendMessageForm()
    context = {
        'form': form,
    }
    return render(request, 'newsletter/send_message.html', context)
