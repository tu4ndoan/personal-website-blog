# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-11 07:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20170825_1516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='feature_image',
            field=models.CharField(default='none', max_length=200),
        ),
    ]