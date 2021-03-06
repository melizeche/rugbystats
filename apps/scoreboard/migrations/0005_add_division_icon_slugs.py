# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-16 09:37
from __future__ import unicode_literals

import autoslug.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scoreboard', '0004_detailed_fields'),
    ]

    operations = [
        migrations.CreateModel(
            name='Division',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name')),
            ],
        ),
        migrations.AddField(
            model_name='team',
            name='icon',
            field=models.ImageField(blank=True, null=True, upload_to='icons'),
        ),
        migrations.AddField(
            model_name='team',
            name='slug',
            field=autoslug.fields.AutoSlugField(blank=True, editable=False, null=True, populate_from='shortname'),
        ),
    ]
