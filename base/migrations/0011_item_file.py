# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-11 16:02
from __future__ import unicode_literals

from django.db import migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_auto_20170411_1215'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='file',
            field=sorl.thumbnail.fields.ImageField(blank=True, upload_to='gallery', verbose_name='Логотип или фоновое изображение'),
        ),
    ]