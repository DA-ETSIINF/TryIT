# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-06 18:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('volunteers', '0003_auto_20180306_1828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volunteer',
            name='shirt_size',
            field=models.CharField(choices=[('s', 'S'), ('m', 'M'), ('l', 'L'), ('xl', 'XL'), ('xxl', 'XXL')], default='m', max_length=250),
        ),
    ]