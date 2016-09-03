# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0007_auto_20160902_0909'),
    ]

    operations = [
        migrations.AddField(
            model_name='propertydetails',
            name='besment',
            field=models.CharField(default=0, max_length=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='propertydetails',
            name='fllors',
            field=models.CharField(default=0, max_length=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='propertydetails',
            name='roof',
            field=models.CharField(default=0, max_length=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='propertydetails',
            name='year_built',
            field=models.CharField(default=0, max_length=5),
            preserve_default=False,
        ),
    ]
