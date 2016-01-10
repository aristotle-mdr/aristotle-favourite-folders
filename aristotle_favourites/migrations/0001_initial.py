# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import autoslug.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('aristotle_mdr', '0010_auto_20160106_1814'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Folder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slug', autoslug.fields.AutoSlugField(populate_from='name', editable=False)),
                ('name', models.CharField(help_text='Folder name', max_length=256)),
                ('description', models.TextField(help_text='Short description for a folder', null=True, blank=True)),
                ('items', models.ManyToManyField(related_name='favourited_in_folder', to='aristotle_mdr._concept', blank=True)),
                ('owner', models.ForeignKey(related_name='favourite_folders', blank=True, to=settings.AUTH_USER_MODEL, help_text='The user a favourites folder belongs too', null=True)),
            ],
        ),
    ]
