from __future__ import unicode_literals
from __future__ import print_function
from __future__ import absolute_import

from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.utils.translation import ugettext_lazy as _
from django.dispatch import receiver
from autoslug import AutoSlugField
from django.utils.encoding import python_2_unicode_compatible

from aristotle_mdr import models as MDR

#@receiver(post_save,sender=MDR._concept)
#@receiver(post_save)
#def do_thing_with_concepts(sender, instance, created, **kwargs):
#    if not issubclass(sender, MDR._concept):
#        return

class Folder(models.Model):
    class Meta:
        ordering = ['name']
    slug = AutoSlugField(populate_from='name',unique_with='owner')
    name = models.CharField(
        help_text = _('Folder name'),
        max_length=256
    )
    description =  models.TextField(
        help_text = _('Short description for a folder'),
        blank=True,
        null=True
    )
    owner = models.ForeignKey(
        User,
        help_text = _('The user a favourites folder belongs too'),
        related_name="favourite_folders"
    )
    items = models.ManyToManyField(
        MDR._concept,
        related_name='favourited_in_folder',
        blank=True
    )

    def __str__(self):
        return "%s (%s)"%(self.name,self.owner.username)