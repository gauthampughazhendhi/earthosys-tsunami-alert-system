# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-15 09:42
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PredictorRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('magnitude', models.FloatField()),
                ('depth', models.FloatField()),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('tsunami', models.BooleanField()),
            ],
        ),
    ]
