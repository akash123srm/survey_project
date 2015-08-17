# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('survey_app', '0014_websiteevaluation_mobility'),
    ]

    operations = [
        migrations.AlterField(
            model_name='websiteevaluation',
            name='mobility',
            field=models.CharField(default=None, max_length=50, choices=[(b'Mobile Context', b'Has this information need been asked in a mobile context, e.g. while being away from home?'), (b'Spatial Coordinates', b'Does this information need contain a reference to a specific location or spatial coordinates?')]),
            preserve_default=True,
        ),
    ]
