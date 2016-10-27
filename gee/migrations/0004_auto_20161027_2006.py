# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-27 17:06
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gee', '0003_auto_20161027_2003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='geendvi',
            name='author',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='anon', to=settings.AUTH_USER_MODEL),
        ),
    ]
