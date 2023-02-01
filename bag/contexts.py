from django.conf import settings
from django.shortcuts import get_object_or_404
from dolls.models import Doll


def bag_contents(request):

    bag_items = []
    total = 0
    doll_count = 0
    bag = request.session.get('bag', {})

    for item_id, quantity in bag.items():
        doll = get_object_or_404(Doll, pk=item_id)
        total += quantity * doll.price
        doll_count += quantity
        bag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'doll': doll,
        })

    grand_total = total

    context = {
        'bag_items': bag_items,
        'total': total,
        'grand_total': grand_total,
        'doll_count': doll_count,
    }

    return context
