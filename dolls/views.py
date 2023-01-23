from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Doll


def all_dolls(request):
    """ A view to show all dolls """

    dolls = Doll.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You did not enter any search criteria!")
                return redirect(reverse('dolls'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            dolls = dolls.filter(queries)

    context = {
        'dolls': dolls,
        'search_term': query,
    }

    return render(request, 'dolls/dolls.html', context)


def doll_detail(request, doll_id):
    """ A view to show individual doll details """

    doll = get_object_or_404(Doll, pk=doll_id)

    context = {
        'doll': doll,
    }

    return render(request, 'dolls/doll_detail.html', context)