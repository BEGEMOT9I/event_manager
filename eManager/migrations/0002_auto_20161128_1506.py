# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-28 15:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eManager', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='addres',
            new_name='address',
        ),
        migrations.RemoveField(
            model_name='event',
            name='city',
        ),
    ]
