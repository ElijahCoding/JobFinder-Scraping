# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-08-27 12:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scraping', '0006_auto_20180715_1046'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='slug',
            field=models.SlugField(blank=True),
        ),
        migrations.AddField(
            model_name='specialty',
            name='slug',
            field=models.SlugField(blank=True),
        ),
    ]