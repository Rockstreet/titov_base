# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-07 10:33
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_category_content'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=1000, verbose_name='Название объекта')),
                ('num', models.IntegerField(blank=True, db_index=True, default=0, verbose_name='Порядковый номер')),
                ('content', ckeditor.fields.RichTextField(blank=True, verbose_name='Описание')),
                ('categories', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='base.Category')),
            ],
            options={
                'ordering': ['num', 'title'],
                'verbose_name_plural': 'Название объекта',
                'verbose_name': 'Название объекта',
            },
        ),
    ]
