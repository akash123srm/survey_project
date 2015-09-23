# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('survey_app', '0022_auto_20150920_1318'),
    ]

    operations = [
        migrations.AddField(
            model_name='websiteevaluation',
            name='completion_code',
            field=models.CharField(help_text='Helps to check if the worker completed his task as desired.', max_length=200, null=True, verbose_name=b'Completion Code', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='websiteevaluation',
            name='time_delta',
            field=models.DateTimeField(default=None, help_text='Helps to find out time difference between when a form is shown and when it is submitted.', verbose_name=b'Time Difference'),
            preserve_default=True,
        ),
    ]
