from django.shortcuts import render, redirect
from .models import Contact
from .forms import ContactForm
from django.contrib import messages


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Details Sent Successfully')
            return redirect('/')
    else:
        form = ContactForm()
    context = {
        'form': form,
    }
    return render(request, 'contact/contact.html', context)
