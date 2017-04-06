# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-06 13:54
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('edited_date', models.DateTimeField(auto_now=True, null=True, verbose_name='Дата редактирования')),
                ('title', models.CharField(default='', max_length=1000, verbose_name='Название')),
                ('content', ckeditor.fields.RichTextField(blank=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name_plural': 'Раздел',
                'verbose_name': 'Раздел',
                'ordering': ['title'],
            },
        ),
    ]
