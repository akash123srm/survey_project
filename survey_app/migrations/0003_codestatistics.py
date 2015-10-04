# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('survey_app', '0002_delete_codestatistics'),
    ]

    operations = [
        migrations.CreateModel(
            name='CodeStatistics',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('completion_code', models.CharField(help_text='Helps to check if the worker completed his task as desired.', max_length=200, null=True, verbose_name=b'Completion Code', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
