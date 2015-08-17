# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('survey_app', '0018_auto_20150623_2027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='websiteevaluation',
            name='mobility',
            field=models.CharField(default=None, max_length=50),
            preserve_default=True,
        ),
    ]
