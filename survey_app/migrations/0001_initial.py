# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
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
                ('name', models.CharField(max_length=100, verbose_name=b'Title of the Website')),
                ('category', models.CharField(max_length=100, verbose_name=b'Category of the Website')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WebsiteEvaluation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_id', models.CharField(help_text='Helps to avoid a user to rate the same URL multiple times during his or her session.', max_length=200, null=True, verbose_name=b'User ID', blank=True)),
                ('time_delta', models.FloatField(default=None, help_text='Helps to find out time difference between when a form is shown and when it is submitted.', null=True, verbose_name=b'The time duration for this url link to get evaluated in minutes', blank=True)),
                ('info_need_identification', models.BooleanField(default=False, help_text=b'Was it possible to identify an information need on the website referenced', verbose_name=b'Information Need Identification')),
                ('time_constraint', models.CharField(default=None, max_length=50, verbose_name=b'Time Constraint', choices=[(b'Hard', b'Hard Constraint'), (b'Soft', b'Soft Constraint'), (b'Independent', b'Independent')])),
                ('answer_validity', models.CharField(default=None, max_length=50, verbose_name=b'Validity of Answer', choices=[(b'Long', b'Long'), (b'Medium', b'Medium'), (b'Short', b'Short')])),
                ('generality_applicability', models.CharField(default=None, max_length=50, verbose_name=b'Generality Of Applicability', choices=[(b'High', b'High Generality'), (b'Medium', b'Medium Generality'), (b'Low', b'Low Generality')])),
                ('location_constraint', models.CharField(default=None, max_length=50, verbose_name=b'Location Constraint', choices=[(b'High', b'High'), (b'Low', b'Low')])),
                ('degree_knowledge', models.CharField(default=None, max_length=50, verbose_name=b'Knowledge Codification', choices=[(b'High', b'High'), (b'Low', b'Low')])),
                ('costs_parameters', models.CharField(default=None, max_length=50, verbose_name=b'Cost Choices', choices=[(b'Fee Based', b'Fee based(i.e., you have to pay for the content)'), (b'Partially Free', b'Partially free(i.e., some services are free, but others require payment)'), (b'Free', b'Free(i.e. no fees occur, all content is available without any fees)')])),
                ('info_provider_layman', models.BooleanField(default=False, help_text=b'Is the provider to the information need a layman?', verbose_name=b'Layman')),
                ('info_provider_operator', models.BooleanField(default=False, help_text=b'Is the provider to the information need an operator?', verbose_name=b'Operator')),
                ('info_provider_expert', models.BooleanField(default=False, help_text=b'Is the provider to the information need an expert?', verbose_name=b'Expert')),
                ('mobile_context', models.BooleanField(default=False, help_text=b'Has this information need been asked in a mobile context, e.g. while being away from home?', verbose_name=b'Mobile Context')),
                ('spatial_coordinates', models.BooleanField(default=False, help_text=b'Does this information need contain a reference to a specific location or spatial coordinates?', verbose_name=b'Spatial Coordinates')),
                ('ask_questions', models.BooleanField(default=False, help_text=b'Can an ordinary user ask question to satisfy his information need?', verbose_name=b'Ask questions')),
                ('suggestions', models.BooleanField(default=False, help_text=b'Does the website give suggestions about content, that was liked,commented on,viewed,posted?', verbose_name=b'Give Suggestions')),
                ('comment', models.BooleanField(default=False, help_text=b'Is there a possibility to rate or comment one the information need?', verbose_name=b'Rate or Comment')),
                ('personal_profile', models.BooleanField(default=False, help_text=b'Is there a possibility to create a personal profile?', verbose_name=b'Create Personal Profile')),
                ('others_information_need', models.BooleanField(default=False, help_text=b'Is it possible to see what kind of information needs other people have or whatkind of information needs they have satisfied before?', verbose_name=b'Others Information Needs')),
                ('contact_user', models.BooleanField(default=False, help_text=b'Is it possible to contact the user, who had the information need?', verbose_name=b'Contact other Users')),
                ('post_url', models.ForeignKey(related_name='evaluation_axis', blank=True, to='survey_app.Post', null=True)),
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
