from django.shortcuts import render, redirect


def view_bag(request):
    """ A view to render shopping bag content page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add product to shopping bag """

    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    for item_id in list(bag.keys()):
        bag[item_id] = item_id

    request.session['bag'] = bag
    return redirect(redirect_url)
