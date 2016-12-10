# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-10 22:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Account', '0003_role_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('address', models.CharField(max_length=32)),
                ('description', models.CharField(max_length=200)),
                ('website', models.CharField(max_length=32)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Account.User')),
            ],
        ),
        migrations.CreateModel(
            name='Sector',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('max_column', models.IntegerField()),
                ('max_row', models.IntegerField()),
            ],
        ),
    ]