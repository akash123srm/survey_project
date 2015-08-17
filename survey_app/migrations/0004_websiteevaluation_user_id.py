# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('survey_app', '0003_auto_20150302_1825'),
    ]

    operations = [
        migrations.AddField(
            model_name='websiteevaluation',
            name='user_id',
            field=models.CharField(default=None, max_length=200, verbose_name=b'User ID'),
            preserve_default=True,
        ),
    ]
