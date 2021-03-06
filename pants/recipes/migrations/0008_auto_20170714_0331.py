# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-14 03:31
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0007_component'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='component',
            name='recipe',
        ),
        migrations.AddField(
            model_name='component',
            name='in_recipe',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='components', to='recipes.Recipe'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='component',
            name='amount',
            field=models.DecimalField(decimal_places=1, help_text='g or ml for ingredients or products; number of serves for recipes', max_digits=5, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
