# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-23 01:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_auto_20170222_1747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='description',
            name='course_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='courses.Course'),
        ),
    ]
