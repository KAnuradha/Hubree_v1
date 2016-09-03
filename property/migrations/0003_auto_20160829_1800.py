# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0002_auto_20160829_1235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property_details',
            name='zip_code',
            field=models.CharField(max_length=15),
        ),
    ]
