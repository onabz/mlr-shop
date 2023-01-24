from django.shortcuts import render, redirect


def view_bag(request):
    """ A view to render shopping bag content page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add product to shopping bag """

    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    request.session['bag'] = bag
    print(request.session['bag'])
    return redirect(redirect_url)
