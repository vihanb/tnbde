# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-07-30 02:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mid', models.IntegerField()),
                ('rid', models.IntegerField(blank=True, null=True)),
                ('room', models.IntegerField()),
                ('date', models.DateField()),
                ('time', models.TimeField(blank=True, null=True)),
                ('content', models.TextField()),
                ('onebox', models.BooleanField(default=False)),
                ('oneboxType', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Username',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transcriptAnalyzer.User')),
            ],
        ),
        migrations.AddField(
            model_name='message',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transcriptAnalyzer.User'),
        ),
    ]
