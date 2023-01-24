from django.shortcuts import render

def view_bag(request):
    """ A view to render shopping bag content page """

    return render(request, 'bag/bag.html')
