# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-25 01:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20170825_0353'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='Name',
            field=models.CharField(default='anonymous', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='comment_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
