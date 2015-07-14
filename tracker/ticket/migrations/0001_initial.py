# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('created_date', models.DateField(auto_now_add=True)),
                ('due_date', models.DateField()),
                ('schedule_date', models.DateField()),
                ('closed', models.BooleanField(default=False)),
            ],
        ),
    ]
