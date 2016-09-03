# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0006_message_shortlistedpropertydetails'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='subject',
            new_name='from_subject',
        ),
        migrations.AddField(
            model_name='message',
            name='to_subject',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
    ]
