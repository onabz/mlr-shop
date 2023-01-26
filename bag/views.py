from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages

from dolls.models import Doll


def view_bag(request):
    """ A view to render shopping bag content page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add product to shopping bag """

    doll = Doll.objects.get(pk=item_id)
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    for item_id in list(bag.keys()):
        bag[item_id] = item_id
        messages.success(request, f'Added {doll.name} to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)


def remove_from_bag(request, item_id):
    """ Remove item from shopping bag """

    try:
        bag.pop(item_id)

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)
