# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact_manager', '0005_auto_20150813_1937'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactprofile',
            name='is_favorite',
        ),
        migrations.AddField(
            model_name='contact',
            name='is_favorite',
            field=models.BooleanField(default=False),
        ),
    ]
