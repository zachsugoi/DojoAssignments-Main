# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-23 02:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_auto_20170222_1751'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='description',
            name='course',
        ),
        migrations.AddField(
            model_name='course',
            name='description',
            field=models.CharField(default='boo', max_length=225),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Description',
        ),
    ]
