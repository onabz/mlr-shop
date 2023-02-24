from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Doll, DollType
from .forms import DollForm


def all_dolls(request):
    """ A view to show all dolls """

    dolls = Doll.objects.all()
    query = None
    dolltype = None

    if request.GET:
        if 'dolltype' in request.GET:
            dolltypes = request.GET['dolltype']
            dolls = dolls.filter(dolltype__name__icontains=dolltypes)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, "You did not enter any search criteria!"
                )
                return redirect(reverse('dolls'))

            queries = Q(name__icontains=query) | Q(
                description__icontains=query
            )
            dolls = dolls.filter(queries)

    context = {
        'dolls': dolls,
        'search_term': query,
        'current_dolltypes': dolltype,
    }

    return render(request, 'dolls/dolls.html', context)


def doll_detail(request, doll_id):
    """ A view to show individual doll details """

    doll = get_object_or_404(Doll, pk=doll_id)

    context = {
        'doll': doll,
    }

    return render(request, 'dolls/doll_detail.html', context)


@login_required
def add_doll(request):
    """ Add a new doll to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only authorized users allowed.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = DollForm(request.POST, request.FILES)
        if form.is_valid():
            doll = form.save()
            messages.success(request, 'Successfully added new doll!')
            return redirect(reverse('doll_detail', args=[doll.id]))
        else:
            messages.error(request,
                           ('Failed to add new doll.'
                            'Please ensure the form is valid.'))
    else:
        form = DollForm()
    template = 'dolls/add_doll.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_doll(request, doll_id):
    """ Edit a doll in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only authorized users allowed.')
        return redirect(reverse('home'))

    doll = get_object_or_404(Doll, pk=doll_id)
    if request.method == 'POST':
        form = DollForm(request.POST, request.FILES, instance=doll)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated doll!')
            return redirect(reverse('doll_detail', args=[doll.id]))
        else:
            messages.error(request,
                           ('Failed to update doll.'
                            'Please ensure the form is valid.'))
    else:
        form = DollForm(instance=doll)
        messages.info(request, f'You are editing {doll.name}')

    template = 'dolls/edit_doll.html'
    context = {
        'form': form,
        'doll': doll,
    }

    return render(request, template, context)


@login_required
def delete_doll(request, doll_id):
    """ Delete a doll from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only authorized users allowed.')
        return redirect(reverse('home'))

    doll = get_object_or_404(Doll, pk=doll_id)
    doll.delete()
    messages.success(request, 'Doll deleted!')
    return redirect(reverse('dolls'))
