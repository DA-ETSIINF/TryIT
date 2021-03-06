# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-11-13 00:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('editions', '0004_auto_20180315_2109'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanySponsorType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'editions_company_sponsortype',
            },
        ),
        migrations.RemoveField(
            model_name='company',
            name='sponsor_type',
        ),
        migrations.AddField(
            model_name='companysponsortype',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='editions.Company'),
        ),
        migrations.AddField(
            model_name='companysponsortype',
            name='edition',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='editions.Edition'),
        ),
        migrations.AddField(
            model_name='companysponsortype',
            name='sponsor_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='editions.SponsorType'),
        ),
        migrations.AddField(
            model_name='company',
            name='sponsor_type',
            field=models.ManyToManyField(through='editions.CompanySponsorType', to='editions.SponsorType'),
        ),
        migrations.AlterUniqueTogether(
            name='companysponsortype',
            unique_together=set([('company', 'edition')]),
        ),
    ]
