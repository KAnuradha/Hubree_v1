# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0004_hubree'),
        ('property', '0004_auto_20160829_1802'),
    ]

    operations = [
        migrations.CreateModel(
            name='PropertyDetails',
            fields=[
                ('property_id', models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, primary_key=True)),
                ('property_title', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=20)),
                ('zip_code', models.CharField(max_length=15)),
                ('home_type', models.CharField(max_length=20, choices=[(b'present type', b'present type'), (b'past type', b'pasttype')])),
                ('beds', models.CharField(max_length=5)),
                ('baths', models.CharField(max_length=5)),
                ('rooms', models.CharField(max_length=5)),
                ('property_size', models.CharField(max_length=20)),
                ('description', models.TextField()),
                ('other_features', models.TextField()),
                ('name', models.ForeignKey(to='registration.Hubree')),
            ],
        ),
        migrations.DeleteModel(
            name='Property_details',
        ),
    ]
