from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from dolls.models import Doll


def view_bag(request):
    """ A view to render shopping bag content page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add product to shopping bag """

    doll = get_object_or_404(Doll, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

    #     messages.success(request, f'Added {doll.name} to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """ Adjust the quantity of the specified product to the specified amount """

    doll = get_object_or_404(Doll, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[item_id] = quantity
    else:
        bag.pop(item_id)

    #     messages.success(request, f'Added {doll.name} to your bag')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """ Remove item from shopping bag """

    try:
        doll = get_object_or_404(Doll, pk=item_id)
        bag = request.session.get('bag', {})
        bag.pop(item_id)
        # messages.success(request, f'Removed {doll.name} from your bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
