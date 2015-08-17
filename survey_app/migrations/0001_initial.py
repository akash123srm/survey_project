# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.URLField(verbose_name=b'Url')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Website',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name=b'Title of the Website')),
                ('slug', models.SlugField(max_length=100, verbose_name=b'URL Name')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WebsiteEvaluation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time_constraint', models.CharField(default=b'Soft', max_length=5, verbose_name=b'Please rate the Time Constraint', choices=[(b'Hard', b'Hard Constraint'), (b'Soft', b'Soft Constraint'), (b'Independent', b'Independent')])),
                ('answer_validity', models.CharField(default=b'Short', max_length=5, verbose_name=b'Please rate the Validity of Answer', choices=[(b'Short', b'Short'), (b'Medium', b'Medium'), (b'Long', b'Long')])),
                ('generality_applicability', models.CharField(default=b'Low', max_length=5, verbose_name=b'Please rate the Generality Of Applicability', choices=[(b'High', b'High'), (b'Medium', b'Medium'), (b'Low', b'Low')])),
                ('location_constraint', models.CharField(default=b'Low', max_length=5, verbose_name=b'Please rate the type of Location Constraint', choices=[(b'High', b'High'), (b'Low', b'Low')])),
                ('degree_knowledge', models.CharField(default=b'Low', max_length=5, verbose_name=b'Please rate the degree of knowledge', choices=[(b'High', b'High'), (b'Low', b'Low')])),
                ('post_url', models.ForeignKey(related_name='evaluation_axis', to='survey_app.Post')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='post',
            name='website',
            field=models.ForeignKey(related_name='urls', to='survey_app.Website'),
            preserve_default=True,
        ),
    ]
