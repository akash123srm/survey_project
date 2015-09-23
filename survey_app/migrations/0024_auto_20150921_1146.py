# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('survey_app', '0023_auto_20150921_1142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='websiteevaluation',
            name='time_delta',
            field=models.TimeField(default=None, help_text='Helps to find out time difference between when a form is shown and when it is submitted.', verbose_name=b'Time Difference'),
            preserve_default=True,
        ),
    ]
