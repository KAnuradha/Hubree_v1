# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0008_auto_20160902_1349'),
    ]

    operations = [
        migrations.RenameField(
            model_name='propertydetails',
            old_name='name',
            new_name='userid',
        ),
    ]
