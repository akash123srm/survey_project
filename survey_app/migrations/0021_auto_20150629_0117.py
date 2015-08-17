# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('survey_app', '0020_auto_20150628_1451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='websiteevaluation',
            name='ask_questions',
            field=models.BooleanField(default=None, help_text=b'Can an ordinary user ask question to satisfy his information need?', verbose_name=b'Ask questions'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='websiteevaluation',
            name='comment',
            field=models.BooleanField(default=None, help_text=b'Is there a possibility to rate or comment one the information need?', verbose_name=b'Rate or Comment'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='websiteevaluation',
            name='contact_user',
            field=models.BooleanField(default=None, help_text=b'Is it possible to contact the user, who had the information need?', verbose_name=b'Contact other Users'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='websiteevaluation',
            name='mobile_context',
            field=models.BooleanField(default=None, help_text=b'Has this information need been asked in a mobile context, e.g. while being away from home?', verbose_name=b'Mobile Context'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='websiteevaluation',
            name='others_information_need',
            field=models.BooleanField(default=None, help_text=b'Is it possible to see what kind of information needs other people have or whatkind of information needs they have satisfied before?', verbose_name=b'Others Information Needs'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='websiteevaluation',
            name='personal_profile',
            field=models.BooleanField(default=None, help_text=b'Is there a possibility to create a personal profile?', verbose_name=b'Create Personal Profile'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='websiteevaluation',
            name='spatial_coordinates',
            field=models.BooleanField(default=None, help_text=b'Does this information need contain a reference to a specific location or spatial coordinates?', verbose_name=b'Spatial Coordinates'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='websiteevaluation',
            name='suggestions',
            field=models.BooleanField(default=None, help_text=b'Does the website give suggestions about content, that was liked,commented on,viewed,posted?', verbose_name=b'Give Suggestions'),
            preserve_default=True,
        ),
    ]
