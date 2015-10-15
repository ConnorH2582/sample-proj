# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact_manager', '0008_auto_20150813_2201'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='url',
            new_name='endpoint',
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.BigIntegerField(),
        ),
    ]
