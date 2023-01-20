from django.shortcuts import render, get_object_or_404
from .models import Doll


def all_dolls(request):
    """ A view to show all dolls """

    dolls = Doll.objects.all()

    context = {
        'dolls': dolls,
    }

    return render(request, 'dolls/dolls.html', context)


def doll_detail(request, doll_id):
    """ A view to show individual doll details """

    doll = get_object_or_404(Doll, pk=doll_id)

    context = {
        'doll': doll,
    }

    return render(request, 'dolls/doll_detail.html', context)