# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0009_auto_20160902_1512'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='name',
            new_name='userid',
        ),
        migrations.RenameField(
            model_name='shortlistedpropertydetails',
            old_name='name',
            new_name='userid',
        ),
    ]
