# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('survey_app', '0008_auto_20150320_0054'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='website',
            name='slug',
        ),
        migrations.AddField(
            model_name='website',
            name='category',
            field=models.CharField(default=None, max_length=100, verbose_name=b'Category of the Website'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='website',
            name='name',
            field=models.CharField(max_length=100, verbose_name=b'Title of the Website'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='websiteevaluation',
            name='answer_validity',
            field=models.CharField(default=None, max_length=50, verbose_name=b'Validity of Answer', choices=[(b'Long', b'Long'), (b'Medium', b'Medium'), (b'Short', b'Short')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='websiteevaluation',
            name='degree_knowledge',
            field=models.CharField(default=None, max_length=50, verbose_name=b'Knowledge Codification', choices=[(b'High', b'High'), (b'Low', b'Low')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='websiteevaluation',
            name='generality_applicability',
            field=models.CharField(default=None, max_length=50, verbose_name=b'Generality Of Applicability', choices=[(b'High', b'High Generality'), (b'Medium', b'Medium Generality'), (b'Low', b'Low Generality')]),
            preserve_default=True,
        ),
    ]
