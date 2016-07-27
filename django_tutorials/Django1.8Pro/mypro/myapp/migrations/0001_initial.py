# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='mymodel',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('index', models.IntegerField(default=0)),
                ('description', models.CharField(max_length=50)),
                ('code', models.CharField(max_length=50)),
            ],
        ),
    ]
