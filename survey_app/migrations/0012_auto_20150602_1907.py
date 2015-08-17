# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('survey_app', '0011_websiteevaluation_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='websiteevaluation',
            name='order',
            field=models.PositiveIntegerField(default=None, null=True, blank=True),
            preserve_default=True,
        ),
    ]
