# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-29 13:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ingredients', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('preparation_mode', models.TextField()),
                ('ingredients', models.ManyToManyField(to='ingredients.Ingredient')),
            ],
        ),
    ]