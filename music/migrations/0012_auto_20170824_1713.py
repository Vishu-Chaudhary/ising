# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-24 11:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0011_auto_20170824_1636'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userlikes',
            name='profile',
        ),
        migrations.RemoveField(
            model_name='userlikes',
            name='song',
        ),
        migrations.DeleteModel(
            name='UserLikes',
        ),
    ]
