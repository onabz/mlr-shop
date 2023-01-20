from django.shortcuts import render
from .models import Doll


def all_dolls(request):
    """ A view to show all dolls """

    dolls = Doll.objects.all()

    context = {
        'dolls': dolls,
    }

    return render(request, 'dolls/dolls.html', context)
