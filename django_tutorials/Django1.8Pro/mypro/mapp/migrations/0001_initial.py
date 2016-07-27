# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='mmodel',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('index', models.IntegerField(default=0)),
                ('desc', models.CharField(max_length=50)),
                ('code', models.CharField(max_length=25)),
            ],
        ),
    ]
