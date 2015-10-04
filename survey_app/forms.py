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
        for fieldname in ['info_need_identification', 'info_provider_layman', 'info_provider_operator', 'info_provider_expert', 'mobile_context','spatial_coordinates','ask_questions','suggestions','comment',
                               'personal_profile', 'others_information_need', 'contact_user']:
                    self.fields[fieldname].help_text = None

    class Meta:
         model = WebsiteEvaluation
         fields = ['time_constraint', 'answer_validity', 'generality_applicability', 'location_constraint',
                   'degree_knowledge', 'costs_parameters','info_need_identification', 'info_provider_layman', 'info_provider_operator',
                   'info_provider_expert', 'mobile_context', 'spatial_coordinates', 'ask_questions', 'suggestions',
                   'comment', 'personal_profile', 'others_information_need', 'contact_user']
         labels = {
            'time_constraint': 'What is the <u>time constraint</u> for the information need or the information addressed in the link above?',
            'answer_validity': 'What is the <u>answer validity</u> for the information need or the information addressed in the link above?',
            'generality_applicability': 'What is the level of <u>generality</u> for the information need or the information addressed in the link above?',
            'location_constraint': 'What is the level of <u>location dependency</u> for the information need or the information addressed in the link above?',
            'degree_knowledge': 'What is the level of <u>knowledge codification</u> for the information need or the information addressed in the link above?',
            'costs_parameters': 'What is the cost structure of the website you visited?',
            'info_need_identification': 'It was possible for me to identify an information need on the website referenced \
             by the link above (an information need describes the problem a person would like to solve).',
            'info_provider_layman': 'Layman- This covers all the lay people that provide information for others.',
            'info_provider_operator':'Operator- This includes all company-information-providers who satisfy information'
                                     ' needs regarding their products or services.',
            'info_provider_expert':'Expert- Someone who has a certain certificate for his/her knowledge, e.g. a doctor, a lawyer, or an editor.',
            'mobile_context': 'This information need has most probably been occurred in a mobile context, i.e. while being away from home or work.',
            'spatial_coordinates': 'This information need contains a reference to a specific location or spatial coordinates.',
            'ask_questions': 'An ordinary user can ask questions on this website to satisfy his/her information needs.',
            'suggestions': 'The website suggests content other users created, liked, commented, or viewed which is similar to mine.',
            'comment': 'It is possible to rate or comment on the information need.',
            'personal_profile': 'It is possible to create a personal profile.',
            'others_information_need': 'It is possible to browse other users information needs.',
            'contact_user': 'It is possible to contact other users who tried to satisfy information needs.'
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