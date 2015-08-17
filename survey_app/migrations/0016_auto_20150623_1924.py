# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('survey_app', '0015_auto_20150623_1840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='websiteevaluation',
            name='mobility',
            field=multiselectfield.db.fields.MultiSelectField(default=None, max_length=50, choices=[(b'Mobile Context', b'Has this information need been asked in a mobile context, e.g. while being away from home?'), (b'Spatial Coordinates', b'Does this information need contain a reference to a specific location or spatial coordinates?')]),
            preserve_default=True,
        ),
    ]
