# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-10 16:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EventCreator', '0002_sector_event'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='img_url',
            field=models.URLField(default='drive.google.com/uc?export=view&id=0Bw48MTtLIo2saUV4c0pDQmZxQXc'),
            preserve_default=False,
        ),
    ]
