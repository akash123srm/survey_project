# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('survey_app', '0009_auto_20150511_1616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='website',
            name='category',
            field=models.CharField(max_length=100, verbose_name=b'Category of the Website'),
            preserve_default=True,
        ),
    ]
