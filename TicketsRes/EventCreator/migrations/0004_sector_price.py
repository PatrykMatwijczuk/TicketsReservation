# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-10 18:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EventCreator', '0003_event_img_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='sector',
            name='price',
            field=models.DecimalField(decimal_places=2, default=69, max_digits=6),
            preserve_default=False,
        ),
    ]