# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import autoslug.fields


class Migration(migrations.Migration):

    dependencies = [
        ('aristotle_favourites', '0003_auto_20160109_2015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='folder',
            name='slug',
            field=autoslug.fields.AutoSlugField(populate_from='name', unique_with=('owner',), editable=False),
        ),
    ]
