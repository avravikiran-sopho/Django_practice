# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-11 06:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist', models.CharField(max_length=200)),
                ('album_title', models.CharField(max_length=200)),
                ('album_logo', models.CharField(max_length=200)),
                ('genere', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_type', models.CharField(max_length=200)),
                ('song_title', models.CharField(max_length=200)),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.Album')),
            ],
        ),
    ]
