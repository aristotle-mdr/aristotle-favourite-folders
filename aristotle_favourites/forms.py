from django import forms
from django.utils.translation import ugettext_lazy as _
from aristotle_favourites.models import Folder
from aristotle_mdr.forms.bulk_actions import BulkActionForm
from aristotle_mdr.perms import user_can_view


class FolderForm(forms.ModelForm):
    class Meta:
        model = Folder
        exclude = ['slug','owner', 'items']


class BulkChangeFromFolder(BulkActionForm):
    classes = 'fa-folder-o'
    confirm_page = 'aristotle_favourites/actions/bulk_add.html'

    folder = forms.ModelChoiceField(
        queryset=Folder.objects.all(),
        label=_("Folder to move to"),
        #widget=autocomplete_light.ChoiceWidget('Autocomplete_concept')
    )

    
    def __init__(self, *args, **kwargs):
        super(BulkAddToFolder, self).__init__(*args, **kwargs)
        # self.queryset = MDR._concept.objects.none()
        self.fields['folder']=forms.ModelChoiceField(
            queryset=self.user.favourite_folders.all(),
            label=_("Folder to move to"),
        )


class BulkAddToFolder(BulkChangeFromFolder):
    action_text = _('Add to folder...')
    classes = 'fa-folder'
    items_label = _('Add the following items to the folder')
    
    folder = forms.ModelChoiceField(
        queryset=Folder.objects.all(),
        label=_("Folder to move to"),
        #widget=autocomplete_light.ChoiceWidget('Autocomplete_concept')
    )

    def make_changes(self):
        folder = self.cleaned_data['folder']
        # self.queryset = folder.items.all()
        items = self.cleaned_data['items']
        bad_items = [str(i.id) for i in items if not user_can_view(self.user, i)]
        items = items.visible(self.user)
        folder.items.add(*items)
        
        return _(
            "%(num_items)s items added to the folder '%(folder_name)s'. \n"
            "Some items failed, they had the id's: %(bad_ids)s"
        ) % {
            'num_items': len(items),
            'bad_ids': ",".join(bad_items),
            'folder_name': folder.name,
        }


class BulkRemoveFromFolder(BulkChangeFromFolder):
    action_text = _('Add to folder...')
    classes = 'fa-folder-o'
    items_label = _('Add the following items to the folder')

    def make_changes(self):
        folder = self.cleaned_data['folder']
        items = self.cleaned_data['items']
        folder.items.remove(*items)
        
        return _(
            "%(num_items)s items removed from the folder '%(folder_name)s'."
        ) % {
            'num_items': len(items),
            'folder_name': folder.name,
        }
