# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_contacts'),
    ]

    operations = [
        migrations.CreateModel(
            name='principal',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('p_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('c_lass', models.CharField(max_length=50)),
                ('pri', models.ForeignKey(to='myapp.principal')),
            ],
        ),
        migrations.CreateModel(
            name='teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('t_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='tea',
            field=models.ManyToManyField(to='myapp.teacher'),
        ),
    ]
