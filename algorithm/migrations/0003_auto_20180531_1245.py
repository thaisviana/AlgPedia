# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-05-31 15:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('algorithm', '0002_auto_20180531_1242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='implementation',
            name='date',
            field=models.DateField(auto_created=True, auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='implementationquestionanswer',
            name='date',
            field=models.DateField(auto_created=True, auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='interest',
            name='date',
            field=models.DateField(auto_created=True, auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='userquestionanswer',
            name='date',
            field=models.DateField(auto_created=True, auto_now_add=True),
        ),
    ]
