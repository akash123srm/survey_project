# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('survey_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='websiteevaluation',
            name='answer_validity',
            field=models.CharField(default=None, max_length=50, verbose_name=b'Validity of Answer', choices=[(b'Short', b'Short'), (b'Medium', b'Medium'), (b'Long', b'Long')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='websiteevaluation',
            name='degree_knowledge',
            field=models.CharField(default=None, max_length=50, verbose_name=b'Degree of Knowledge', choices=[(b'High', b'High'), (b'Low', b'Low')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='websiteevaluation',
            name='generality_applicability',
            field=models.CharField(default=None, max_length=50, verbose_name=b'Generality Of Applicability', choices=[(b'High', b'High'), (b'Medium', b'Medium'), (b'Low', b'Low')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='websiteevaluation',
            name='location_constraint',
            field=models.CharField(default=None, max_length=50, verbose_name=b'Location Constraint', choices=[(b'High', b'High'), (b'Low', b'Low')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='websiteevaluation',
            name='time_constraint',
            field=models.CharField(default=None, max_length=50, verbose_name=b'Time Constraint', choices=[(b'Hard', b'Hard Constraint'), (b'Soft', b'Soft Constraint'), (b'Independent', b'Independent')]),
            preserve_default=True,
        ),
    ]
