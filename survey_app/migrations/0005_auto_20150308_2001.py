# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('survey_app', '0004_websiteevaluation_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='websiteevaluation',
            name='user_id',
            field=models.CharField(default=None, max_length=200, null=True, verbose_name=b'User ID', blank=True),
            preserve_default=True,
        ),
    ]