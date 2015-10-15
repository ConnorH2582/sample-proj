# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact_manager', '0006_auto_20150813_1938'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactprofile',
            name='contact',
        ),
        migrations.AddField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=254, unique=True, default=None),
        ),
        migrations.AddField(
            model_name='contact',
            name='phone',
            field=models.IntegerField(default=None),
        ),
        migrations.DeleteModel(
            name='ContactProfile',
        ),
    ]
