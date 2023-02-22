from django.shortcuts import render, redirect
from .models import Newsletter, SendMessage
from .forms import NewsletterForm, SendMessageForm
from django.contrib import messages


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
    form = SendMessageForm()
    context = {
        'form': form,
    }
    return render(request, 'newsletter/send_message.html', context)
