# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('survey_app', '0025_auto_20150922_1440'),
    ]

    operations = [
        migrations.AlterField(
            model_name='websiteevaluation',
            name='time_delta',
            field=models.CharField(default=None, max_length=200, blank=True, help_text='Helps to find out time difference between when a form is shown and when it is submitted.', null=True, verbose_name=b'Time Difference'),
            preserve_default=True,
        ),
    ]
