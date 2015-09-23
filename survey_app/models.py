from django.db import models
import datetime
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from .enums import (TimeConstraint, AnswerValidity,
                   GeneralityApplicability, LocationConstraint,
                   DegreeKnowledge,CostsParameters)

# Create your models here.

class Website(models.Model):
    name = models.CharField('Title of the Website', max_length=100)
    category = models.CharField('Category of the Website',max_length=100)

    def __str__(self):
        return "%s" % self.name

class WebsiteEvaluation(models.Model):
    user_id = models.CharField('User ID', max_length=200, null=True, blank=True,
              help_text=_('Helps to avoid a user to rate the same URL multiple times during his or her session.'))

    completion_code = models.CharField('Completion Code', max_length=200, null=True, blank=True,
              help_text=_('Helps to check if the worker completed his task as desired.'))

    time_delta = models.IntegerField('The time duration for this url link to get evaluated in minutes', null=True, blank=True, default=None,
                                  help_text=_('Helps to find out time difference between '
                                             'when a form is shown and when it is submitted.'))

    post_url = models.ForeignKey('Post',related_name='evaluation_axis',null=True,blank=True)

    TIME_CONSTRAINT_CHOICES = (
        (TimeConstraint.HARD_CONSTRAINT, 'Hard Constraint'),
        (TimeConstraint.SOFT_CONSTRAINT, 'Soft Constraint'),
        (TimeConstraint.INDEPENDENT, 'Independent')
        )

    ANSWER_VALIDITY_CHOICES = (
        (AnswerValidity.LONG, 'Long'),
        (AnswerValidity.MEDIUM, 'Medium'),
        (AnswerValidity.SHORT, 'Short')
        )

    GENERALITY_OF_APPLICABILITY_CHOICES = (
        (GeneralityApplicability.HIGH, 'High Generality'),
        (GeneralityApplicability.MEDIUM, 'Medium Generality'),
        (GeneralityApplicability.LOW, 'Low Generality')
        )

    LOCATION_CONSTRAINT_CHOICES = (
        (LocationConstraint.HIGH, 'High'),
        (LocationConstraint.LOW, 'Low')
        )

    DEGREE_OF_KNOWLEDGE_CHOICES = (
        (DegreeKnowledge.HIGH, 'High'),
        (DegreeKnowledge.LOW, 'Low')
        )

    COST_CHOICES = (
        (CostsParameters.FEE_BASED, 'Fee based(i.e., you have to pay for the content)'),
        (CostsParameters.PARTIALLY_FREE, 'Partially free(i.e., some services are free, but others require payment)'),
        (CostsParameters.FREE, 'Free(i.e. no fees occur, all content is available without any fees)')
    )

    info_need_identification =  models.BooleanField('Information Need Identification',default=False,
                    help_text='Was it possible to identify an information need on the website referenced')

    time_constraint = models.CharField('Time Constraint',max_length=50,
                                      choices= TIME_CONSTRAINT_CHOICES,
                                      default=None)

    answer_validity = models.CharField('Validity of Answer',max_length=50,
                                      choices= ANSWER_VALIDITY_CHOICES,
                                      default=None)

    generality_applicability = models.CharField('Generality Of Applicability',max_length=50,
                                      choices=GENERALITY_OF_APPLICABILITY_CHOICES ,
                                      default=None)

    location_constraint = models.CharField('Location Constraint',max_length=50,
                                      choices=LOCATION_CONSTRAINT_CHOICES,
                                      default=None)

    degree_knowledge = models.CharField('Knowledge Codification',max_length=50,
                                      choices=DEGREE_OF_KNOWLEDGE_CHOICES,
                                      default=None)
    #Costs Parameters

    costs_parameters = models.CharField('Cost Choices',max_length=50,
                                      choices=COST_CHOICES,
                                      default=None)

    #Information Provider Parameters

    """info_provider = models.CharField('Information Provider Choices',max_length=50,
                                      choices=INFORMATION_PROVIDER_CHOICES,
                                      default=None)"""

    info_provider_layman = models.BooleanField('Layman',default=False,
                    help_text='Is the provider to the information need a layman?')

    info_provider_operator = models.BooleanField('Operator',default=False,
                    help_text='Is the provider to the information need an operator?')

    info_provider_expert = models.BooleanField('Expert',default=False,
                    help_text='Is the provider to the information need an expert?')

    # Mobility parameters
    mobile_context = models.BooleanField('Mobile Context',default=False,
                     help_text='Has this information need been asked in a mobile context, e.g. while being away from home?')

    spatial_coordinates = models.BooleanField('Spatial Coordinates',default=False,
                          help_text='Does this information need contain a reference to a specific location or spatial coordinates?')

    # Sociality parameters
    ask_questions = models.BooleanField('Ask questions',default=False,
                    help_text='Can an ordinary user ask question to satisfy his information need?')

    suggestions = models.BooleanField('Give Suggestions',default=False,
                  help_text='Does the website give suggestions about content, that was liked,commented on,viewed,posted?')

    comment = models.BooleanField('Rate or Comment',default=False,
              help_text='Is there a possibility to rate or comment one the information need?')

    personal_profile = models.BooleanField('Create Personal Profile',default=False,
                       help_text='Is there a possibility to create a personal profile?')

    others_information_need = models.BooleanField('Others Information Needs',default=False,
                              help_text='Is it possible to see what kind of information needs other people have or what'
                                        'kind of information needs they have satisfied before?')

    contact_user = models.BooleanField('Contact other Users',default=False,
                   help_text='Is it possible to contact the user, who had the information need?')


    def is_time_duration_valid(self):
        return not self.time_delta < 2
    is_time_duration_valid.admin_order_field = 'time_delta'
    is_time_duration_valid.boolean = True
    is_time_duration_valid.short_description = 'Was the time to fill the questions valid'

    def __str__(self):
        return "%s" % self.post_url


class Post(models.Model):
    url = models.URLField('Url',max_length=200)
    website = models.ForeignKey(Website,related_name='urls')

    def get_url_count(self):
        evaluations = [w.post_url for w in WebsiteEvaluation.objects.all()]
        return evaluations.count(self)

    def __str__(self):
        return "%s" % self.url
