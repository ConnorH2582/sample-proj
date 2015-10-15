# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact_manager', '0003_auto_20150813_1621'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='nameyear',
            field=models.CharField(default=None, max_length=204),
            preserve_default=False,
        ),
    ]
