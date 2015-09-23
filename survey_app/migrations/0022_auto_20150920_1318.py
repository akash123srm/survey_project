# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('survey_app', '0021_auto_20150629_0117'),
    ]

    operations = [
        migrations.AddField(
            model_name='websiteevaluation',
            name='costs_parameters',
            field=models.CharField(default=None, max_length=50, verbose_name=b'Cost Choices', choices=[(b'Fee Based', b'Fee based(i.e., you have to pay for the content)'), (b'Partially Free', b'Partially free(i.e., some services are free, but others require payment)'), (b'Free', b'Free(i.e. no fees occur, all content is available without any fees)')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='websiteevaluation',
            name='info_need_identification',
            field=models.BooleanField(default=False, help_text=b'Was it possible to identify an information need on the website referenced', verbose_name=b'Information Need Identification'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='websiteevaluation',
            name='info_provider_expert',
            field=models.BooleanField(default=False, help_text=b'Is the provider to the information need an expert?', verbose_name=b'Expert'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='websiteevaluation',
            name='info_provider_layman',
            field=models.BooleanField(default=False, help_text=b'Is the provider to the information need a layman?', verbose_name=b'Layman'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='websiteevaluation',
            name='info_provider_operator',
            field=models.BooleanField(default=False, help_text=b'Is the provider to the information need an operator?', verbose_name=b'Operator'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='websiteevaluation',
            name='ask_questions',
            field=models.BooleanField(default=False, help_text=b'Can an ordinary user ask question to satisfy his information need?', verbose_name=b'Ask questions'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='websiteevaluation',
            name='comment',
            field=models.BooleanField(default=False, help_text=b'Is there a possibility to rate or comment one the information need?', verbose_name=b'Rate or Comment'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='websiteevaluation',
            name='contact_user',
            field=models.BooleanField(default=False, help_text=b'Is it possible to contact the user, who had the information need?', verbose_name=b'Contact other Users'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='websiteevaluation',
            name='mobile_context',
            field=models.BooleanField(default=False, help_text=b'Has this information need been asked in a mobile context, e.g. while being away from home?', verbose_name=b'Mobile Context'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='websiteevaluation',
            name='others_information_need',
            field=models.BooleanField(default=False, help_text=b'Is it possible to see what kind of information needs other people have or whatkind of information needs they have satisfied before?', verbose_name=b'Others Information Needs'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='websiteevaluation',
            name='personal_profile',
            field=models.BooleanField(default=False, help_text=b'Is there a possibility to create a personal profile?', verbose_name=b'Create Personal Profile'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='websiteevaluation',
            name='spatial_coordinates',
            field=models.BooleanField(default=False, help_text=b'Does this information need contain a reference to a specific location or spatial coordinates?', verbose_name=b'Spatial Coordinates'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='websiteevaluation',
            name='suggestions',
            field=models.BooleanField(default=False, help_text=b'Does the website give suggestions about content, that was liked,commented on,viewed,posted?', verbose_name=b'Give Suggestions'),
            preserve_default=True,
        ),
    ]
