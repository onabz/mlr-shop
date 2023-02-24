import random
from django.shortcuts import render
from .models import Saying


def index(request):
    """ A view to return the index page """
    sayings = list(Saying.objects.all())
    random_message = random.choice(sayings)
    template = 'home/index.html'
    context = {
        'message': random_message
    }
    return render(request, template, context)
