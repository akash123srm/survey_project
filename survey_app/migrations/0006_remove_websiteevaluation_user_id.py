# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('survey_app', '0005_auto_20150308_2001'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='websiteevaluation',
            name='user_id',
        ),
    ]
