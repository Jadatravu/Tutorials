# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mapp', '0002_mmodel_nmember'),
    ]

    operations = [
        migrations.CreateModel(
            name='cmodel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('year', models.IntegerField(default=0)),
                ('name', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=25)),
                ('department', models.CharField(max_length=25)),
            ],
        ),
    ]
