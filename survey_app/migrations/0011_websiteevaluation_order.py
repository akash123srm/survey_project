# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('survey_app', '0010_auto_20150511_1623'),
    ]

    operations = [
        migrations.AddField(
            model_name='websiteevaluation',
            name='order',
            field=models.PositiveIntegerField(default=None),
            preserve_default=True,
        ),
    ]
