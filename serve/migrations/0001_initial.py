# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-21 01:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='database',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice_no', models.CharField(max_length=500, null=True)),
                ('dated', models.CharField(max_length=500, null=True)),
                ('party_details', models.CharField(max_length=500, null=True)),
                ('party_tin', models.CharField(max_length=500, null=True)),
                ('transport', models.CharField(max_length=500, null=True)),
                ('station', models.CharField(max_length=500, null=True)),
                ('name', models.CharField(max_length=500, null=True)),
                ('qty', models.CharField(max_length=500, null=True)),
                ('unit', models.CharField(max_length=500, null=True)),
                ('price', models.CharField(max_length=500, null=True)),
                ('gst', models.CharField(max_length=500, null=True)),
            ],
        ),
    ]