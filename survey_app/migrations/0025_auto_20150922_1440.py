# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('survey_app', '0024_auto_20150921_1146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='websiteevaluation',
            name='time_delta',
            field=models.TimeField(default=None, help_text='Helps to find out time difference between when a form is shown and when it is submitted.', null=True, verbose_name=b'Time Difference', blank=True),
            preserve_default=True,
        ),
    ]
