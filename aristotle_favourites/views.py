from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.views.generic import TemplateView

from aristotle_favourites.forms import FolderForm
from aristotle_favourites.models import Folder
from aristotle_mdr.views.utils import paginated_list

from aristotle_mdr import models as MDR
from aristotle_mdr.perms import user_can_view
from aristotle_mdr.utils import url_slugify_concept


@login_required
def all_folders(request):
    return render(request,"aristotle_favourites/dashboard/all_folders.html",{})


@login_required
def quick_favourites(request):
    from aristotle_mdr.views.user_pages import favourites
    return favourites(request)


@login_required
def add_folder(request):
    if request.method == 'POST':  # If the form has been submitted...
        form = FolderForm(request.POST,initial={'owner':request.user})
        if form.is_valid():
            folder = form.save(commit=False)
            folder.owner = request.user
            folder.save()
            return redirect(reverse('aristotle_favourites:view_folder',args=[folder.slug]))

    else:
        form = FolderForm()

    return render(
        request,
        "aristotle_favourites/actions/new_folder.html",
        {'form':form}
    )


@login_required
def view_folder(request,folder_slug):
    # a user can only ever see their own items
    folder = get_object_or_404(Folder,slug=folder_slug,owner=request.user)
    context = {'folder':folder}
    return paginated_list(
        request,
        folder.items,
        "aristotle_favourites/dashboard/view_folder.html",
        context
    )


@login_required
def toggle_item_in_folder(request,folder_slug):
    item_id = request.GET.get('item',None)
    item = get_object_or_404(MDR._concept, pk=item_id).item
    folder = get_object_or_404(Folder,slug=folder_slug,owner=request.user)

    if not user_can_view(request.user, item):
        if request.user.is_anonymous():
            return redirect(reverse('friendly_login') + '?next=%s' % request.path)
        else:
            raise PermissionDenied
    
    if folder.items.filter(pk=item.id).exists():
        folder.items.remove(item)
    else:
        folder.items.add(item)

    if request.GET.get('next', None):
        return redirect(request.GET.get('next'))
    return redirect(url_slugify_concept(item))
