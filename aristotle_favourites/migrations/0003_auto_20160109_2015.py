# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('aristotle_favourites', '0002_add_folder_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='folder',
            name='owner',
            field=models.ForeignKey(related_name='favourite_folders', to=settings.AUTH_USER_MODEL, help_text='The user a favourites folder belongs too'),
        ),
    ]
