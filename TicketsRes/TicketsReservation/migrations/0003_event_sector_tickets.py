# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-10 22:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Account', '0003_role_user'),
        ('TicketsReservation', '0002_auto_20161210_2300'),
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
        migrations.CreateModel(
            name='Tickets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('column', models.IntegerField()),
                ('row', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('guest_name', models.CharField(max_length=32)),
                ('guest_surname', models.CharField(max_length=32)),
                ('guest_email', models.CharField(max_length=32)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TicketsReservation.Event')),
                ('sector', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TicketsReservation.Sector')),
            ],
        ),
    ]