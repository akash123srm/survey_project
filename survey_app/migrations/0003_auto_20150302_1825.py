# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('survey_app', '0002_auto_20150302_1802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='websiteevaluation',
            name='post_url',
            field=models.ForeignKey(related_name='evaluation_axis', blank=True, to='survey_app.Post', null=True),
            preserve_default=True,
        ),
    ]
