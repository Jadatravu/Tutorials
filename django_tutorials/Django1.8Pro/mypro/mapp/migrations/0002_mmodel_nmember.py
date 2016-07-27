# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mmodel',
            name='nmember',
            field=models.CharField(max_length=25, default='qwerty'),
            preserve_default=False,
        ),
    ]
