# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('survey_app', '0017_auto_20150623_1951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='websiteevaluation',
            name='mobility',
            field=models.BooleanField(default=None),
            preserve_default=True,
        ),
    ]
