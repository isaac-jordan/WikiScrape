# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='wikipediapage',
            name='parent_page',
            field=models.ForeignKey(default=b'', to='pages.WikipediaPage'),
            preserve_default=True,
        ),
    ]
