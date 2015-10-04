# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('survey_app', '0003_codestatistics'),
    ]

    operations = [
        migrations.AddField(
            model_name='codestatistics',
            name='worker',
            field=models.CharField(default=2, max_length=200, verbose_name=b'Worker ID'),
            preserve_default=False,
        ),
    ]
