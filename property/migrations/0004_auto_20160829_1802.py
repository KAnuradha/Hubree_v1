# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0003_auto_20160829_1800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property_details',
            name='baths',
            field=models.CharField(max_length=5),
        ),
        migrations.AlterField(
            model_name='property_details',
            name='beds',
            field=models.CharField(max_length=5),
        ),
        migrations.AlterField(
            model_name='property_details',
            name='rooms',
            field=models.CharField(max_length=5),
        ),
    ]
