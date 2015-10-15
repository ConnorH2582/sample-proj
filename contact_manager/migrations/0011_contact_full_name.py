# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact_manager', '0010_auto_20150813_2233'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='full_name',
            field=models.CharField(max_length=60, default=None),
        ),
    ]
