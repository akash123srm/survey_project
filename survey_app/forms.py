from django import forms
from django.forms import ModelForm
from django_select2.fields import ModelSelect2Field, ModelSelect2MultipleField, Select2ChoiceField
from django_select2.widgets import Select2Widget, Select2MultipleWidget
from .models import Website,Post ,WebsiteEvaluation
from django.utils.translation import ugettext_lazy as _
from django.utils.safestring import mark_safe

class EvaluationForm(ModelForm):

    def __init__(self, *args, **kwargs):
             super(EvaluationForm, self).__init__(*args, **kwargs)
             for fieldname in ['info_provider_layman','info_provider_operator','info_provider_expert','mobile_context','spatial_coordinates','ask_questions','suggestions','comment',
                               'personal_profile','others_information_need','contact_user']:
                    self.fields[fieldname].help_text = None

    class Meta:
         model = WebsiteEvaluation
         fields = ['time_constraint', 'answer_validity','generality_applicability','location_constraint',
                   'degree_knowledge','costs_parameters','info_provider_layman','info_provider_operator',
                   'info_provider_expert','mobile_context','spatial_coordinates','ask_questions','suggestions',
                   'comment','personal_profile','others_information_need','contact_user']
         labels = {
            'time_constraint': 'What is the <u>time constraint</u> for the URL listed above?',
            'answer_validity': 'What is the <u>answer validity</u> for the URL listed above?',
            'generality_applicability': 'What is the level of <u>generality</u> for the URL listed above?',
            'location_constraint': 'What is the level of <u>location dependency</u> for the URL listed above?',
            'degree_knowledge': 'What is the level of <u>knowledge codification</u> for the URL listed above?',
            'costs_parameters': 'What should be the category of cost?',
            'info_provider_layman': 'Is the provider to the above information need a <strong>Layman</strong>?',
            'info_provider_operator':'Is the provider to the above information need an <strong>Operator</strong>?',
            'info_provider_expert':'Is the provider to the above information need an <strong>Expert</strong>?',
            'mobile_context': 'Has this information need been asked in a mobile context, e.g. while being away from home?',
            'spatial_coordinates': 'Does this information need contain a reference to a specific location or spatial coordinates?',
            'ask_questions': 'Can an ordinary user ask question to satisfy his information need?',
            'suggestions': 'Does the website give suggestions about content, that was liked, commented on, viewed, posted '
                           'or offered by other users, whose behaviour or interests are similar to mine?',
            'comment': 'Is there a possibility to rate or comment one the information need?',
            'personal_profile': 'Is there a possibility to create a personal profile?',
            'others_information_need': 'Is it possible to see what kind of information needs other people have or what'
                                        'kind of information needs they have satisfied before?',
            'contact_user': 'Is it possible to contact the user, who had the information need?'
            }

         widgets = {
            'time_constraint': forms.RadioSelect(),
            'answer_validity': forms.RadioSelect(),
            'generality_applicability': forms.RadioSelect(),
            'location_constraint': forms.RadioSelect(),
            'degree_knowledge': forms.RadioSelect(),
            'costs_parameters': forms.RadioSelect(),
            }



class PostAdminForm(forms.ModelForm):
    """website = ModelSelect2Field(
        queryset=Website.objects,
        widget=Select2Widget(
            select2_options={
                'width': '220px',
                }
        )
    )"""

class WebsiteEvaluationAdminForm(forms.ModelForm):

    class Meta:
        widgets = {
            'time_constraint': forms.RadioSelect(),
            'answer_validity': forms.RadioSelect(),
            'generality_applicability': forms.RadioSelect(),
            'location_constraint': forms.RadioSelect(),
            'degree_knowledge': forms.RadioSelect(),
            'costs_parameters': forms.RadioSelect(),
            }

    """ def clean_mobility(self):
        mobility = self.cleaned_data['mobility']
        # mobility = '  '.join(mobility)
        return mobility"""

    """ post_url = ModelSelect2Field(
        queryset=Post.objects,
        widget=Select2Widget(
            select2_options={
                'width': '220px',
                }
        )
    )"""