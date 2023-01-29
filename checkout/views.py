from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There is nothing in your bag")
        return redirect(reverse('dolls'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51MVbQwJDbOhf0bAhrpA38YaUHVOI2z9wRP2kRCvwRToBkaDTVwc2rJCF6pGX8VpxaTj1WmqzTPCmElxWaJ0SYIzI00bz191WYU',
        'client_secret': 'sk_test_51MVbQwJDbOhf0bAhWMuIR6c7NnBQlui8kyk5fuIMb51A0ENpS2KogXVBfqNMnbCRX0W9zDvVsooYDkNdxhHq0mkF00L3q27myj',
    }

    return render(request, template, context)
