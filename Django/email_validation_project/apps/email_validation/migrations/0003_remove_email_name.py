# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-23 21:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('email_validation', '0002_email_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='email',
            name='name',
        ),
    ]