# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('survey_app', '0012_auto_20150602_1907'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='websiteevaluation',
            name='order',
        ),
    ]
