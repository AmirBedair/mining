# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-26 15:31
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mining', '0002_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='mdate',
            field=models.DateTimeField(default=datetime.datetime(2016, 11, 26, 15, 31, 11, 943603), verbose_name='date published'),
            preserve_default=False,
        ),
    ]