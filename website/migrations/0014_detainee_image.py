# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-11 16:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0013_report_session'),
    ]

    operations = [
        migrations.AddField(
            model_name='detainee',
            name='image',
            field=models.ImageField(default=1, upload_to=b'%m/%d'),
            preserve_default=False,
        ),
    ]
