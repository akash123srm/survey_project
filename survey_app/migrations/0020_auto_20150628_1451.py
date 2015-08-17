# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('survey_app', '0019_auto_20150623_2033'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='websiteevaluation',
            name='mobility',
        ),
        migrations.AddField(
            model_name='websiteevaluation',
            name='ask_questions',
            field=models.BooleanField(default=None, verbose_name=b'Ask questions'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='websiteevaluation',
            name='comment',
            field=models.BooleanField(default=None, verbose_name=b'Rate or Comment'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='websiteevaluation',
            name='contact_user',
            field=models.BooleanField(default=None, verbose_name=b'Contact other Users'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='websiteevaluation',
            name='mobile_context',
            field=models.BooleanField(default=None, verbose_name=b'Mobile Context'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='websiteevaluation',
            name='others_information_need',
            field=models.BooleanField(default=None, verbose_name=b'Is it possible to see what others information needs are'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='websiteevaluation',
            name='personal_profile',
            field=models.BooleanField(default=None, verbose_name=b'Create Personal Profile'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='websiteevaluation',
            name='spatial_coordinates',
            field=models.BooleanField(default=None, verbose_name=b'Spatial Coordinates'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='websiteevaluation',
            name='suggestions',
            field=models.BooleanField(default=None, verbose_name=b'Give Suggestions'),
            preserve_default=True,
        ),
    ]
