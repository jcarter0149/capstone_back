# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-07 16:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_profile_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='role',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='team',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]