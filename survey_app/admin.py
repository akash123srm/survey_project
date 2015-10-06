import csv
import math
import operator
from django.contrib import admin
# Register your models here.
from .models import Website, Post, WebsiteEvaluation, CodeStatistics
from .forms import PostAdminForm, WebsiteEvaluationAdminForm
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from django.contrib.admin import AdminSite
from django.contrib.sites.models import Site
from django_tables2.config import RequestConfig
from .tables import WebsiteEvaluationTable
from django.utils.encoding import smart_str
from django.http import HttpResponse
from itertools import chain
from collections import defaultdict
from django.db.models import Count
from .enums import (TimeConstraint, AnswerValidity,
                   GeneralityApplicability, LocationConstraint,
                   DegreeKnowledge)


class WebsiteAdmin(admin.ModelAdmin):
    list_display = ['name', 'category']
    list_filter = ['name','category']


class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm
    list_display = ['url','show_website']
    list_filter = ['url','website']

    def show_website(self, obj):
        return '<a href="%s">%s</a>' % (reverse('admin:survey_app_website_change', args=[obj.website.pk]), obj.website)
    show_website.allow_tags = True
    show_website.short_description = _('Website')


class WebsiteEvaluationAdmin(admin.ModelAdmin):

    form = WebsiteEvaluationAdminForm
    list_display = ['post_url','time_delta','time_constraint','is_time_duration_valid','answer_validity',
                    'generality_applicability','location_constraint',
                    'degree_knowledge','costs_parameters','info_need_identification','info_provider_layman','info_provider_operator','info_provider_expert',
                    'mobile_context','spatial_coordinates','ask_questions','suggestions','comment',
                    'personal_profile','others_information_need','contact_user','user_id']

    list_filter = ['post_url', 'time_delta', 'time_constraint', 'answer_validity',
                   'generality_applicability', 'location_constraint',
                   'degree_knowledge','costs_parameters','info_need_identification','info_provider_layman','info_provider_operator','info_provider_expert',
                   'mobile_context','spatial_coordinates','ask_questions','suggestions','comment',
                   'personal_profile','others_information_need','contact_user','user_id']

    actions = ['export_csv', 'aggregate_data', 'export_time_statistics']

    def aggregate_data(self, request, queryset):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=aggregated_data.csv'
        writer = csv.writer(response, csv.excel)
        response.write(u'\ufeff'.encode('utf8')) # BOM (optional...Excel needs it to open UTF-8 file properly)"""
        result_dict = {}
        dict_time_constraint= {"Independent": 0, "Soft": 1,
                              "Hard": 2}
        dict_answer_validity = {"Short": 0, "Medium": 1,
                              "Long": 2}
        dict_generality_applicability = {"Low": 0, "Medium": 1,
                              "High": 2}
        dict_location_constraint =  {"Low": 0, "High": 1}
        dict_degree_knowledge = dict_location_constraint.copy()
        dict_boolean = {False: 0, True: 1}
        #dict_mobility_sociality = dict_boolean.copy()
        dict_costs_parameters = {"Free": 0, "Partially Free": 1, "Fee Based": 2}
        dict_info_provider = dict_mobility_sociality = dict_boolean.copy()
        posts_evaluated = list(set([p.post_url for p in WebsiteEvaluation.objects.all()]))
        #print posts_evaluated
        print dict_info_provider
        list_test=[p.evaluation_axis.all() for p in posts_evaluated]
        print list_test
        for i in list_test:
            result_dict[i[0]]=[[x.post_url.website.name,x.post_url.website.category,x.post_url,x.time_constraint,x.answer_validity,x.generality_applicability,
                                x.location_constraint, x.degree_knowledge,x.costs_parameters,x.info_provider_layman,x.info_provider_operator,
                                x.info_provider_expert,x.mobile_context,x.spatial_coordinates,x.ask_questions,x.suggestions,
                                x.comment,x.personal_profile,x.others_information_need,x.contact_user] for x in i]
        website_list=[]
        category_list=[]
        url_list=[]
        result_list=[]
        #print result_dict
        for key in result_dict.keys():
            """self.total_time_constraint_count=0
            self.total_answer_validity_count=0
            self.total_generality_applicability_count=0
            self.total_location_constraint_count=0
            self.total_degree_knowledge_count=0
            self.total_costs_parameters_count=0
            self.total_info_provider_layman_count=0
            self.total_info_provider_operator_count=0
            self.total_info_provider_expert_count=0
            self.total_mobile_context_count=0
            self.total_spatial_coordinates_count=0
            self.total_ask_questions_count=0
            self.total_suggestions_count=0
            self.total_comment_count=0
            self.total_personal_profile_count=0
            self.total_others_information_need_count=0
            self.total_contact_user_count=0"""

            self.total_time_constraint_count=self.total_answer_validity_count=self.total_generality_applicability_count\
            =self.total_location_constraint_count=self.total_degree_knowledge_count=self.total_costs_parameters_count\
            =self.total_info_provider_layman_count=self.total_info_provider_operator_count=self.total_info_provider_expert_count\
            =self.total_mobile_context_count=self.total_spatial_coordinates_count=self.total_ask_questions_count=self.total_suggestions_count\
            =self.total_comment_count=self.total_personal_profile_count=self.total_others_information_need_count=self.total_contact_user_count=0

            print result_dict[key]

            for rating in result_dict[key]:
                self.website = rating[0]
                self.category = rating[1]
                self.url = rating[2]
                self.total_time_constraint_count+=dict_time_constraint[rating[3]]
                self.total_answer_validity_count+=dict_answer_validity[rating[4]]
                self.total_generality_applicability_count+=dict_generality_applicability[rating[5]]
                self.total_location_constraint_count+=dict_location_constraint[rating[6]]
                self.total_degree_knowledge_count+=dict_degree_knowledge[rating[7]]
                self.total_costs_parameters_count+=dict_costs_parameters[rating[8]]
                self.total_info_provider_layman_count+=dict_info_provider[rating[9]]
                self.total_info_provider_operator_count+=dict_info_provider[rating[10]]
                self.total_info_provider_expert_count+=dict_info_provider[rating[11]]
                self.total_mobile_context_count+=dict_mobility_sociality[rating[12]]
                self.total_spatial_coordinates_count+=dict_mobility_sociality[rating[13]]
                self.total_ask_questions_count+=dict_mobility_sociality[rating[14]]
                self.total_suggestions_count+=dict_mobility_sociality[rating[15]]
                self.total_comment_count+=dict_mobility_sociality[rating[16]]
                self.total_personal_profile_count+=dict_mobility_sociality[rating[17]]
                self.total_others_information_need_count+=dict_mobility_sociality[rating[18]]
                self.total_contact_user_count+=dict_mobility_sociality[rating[19]]

            total_calc = [self.total_time_constraint_count, self.total_answer_validity_count,
                          self.total_generality_applicability_count,self.total_location_constraint_count,
                          self.total_degree_knowledge_count,self.total_costs_parameters_count,self.total_info_provider_layman_count,
                          self.total_info_provider_operator_count,self.total_info_provider_expert_count,self.total_mobile_context_count,self.total_spatial_coordinates_count, self.total_ask_questions_count,
                          self.total_suggestions_count,self.total_comment_count, self.total_personal_profile_count,
                          self.total_others_information_need_count,self.total_contact_user_count]

            avg = [a/float(len(result_dict[key])) for a in total_calc]
            result_list.append(avg)
            website_list.append(self.website)
            category_list.append(self.category)
            url_list.append(self.url)

        writer.writerow([
        smart_str(u"Website"),
        smart_str(u"Category"),
        smart_str(u"Url"),
        smart_str(u"Time Constraint"),
        smart_str(u"Answer Validity"),
        smart_str(u"Generality Of Applicability"),
        smart_str(u"Location Dependency"),
        smart_str(u"Knowledge Codification"),
        smart_str(u"Costs Category"),
        smart_str(u"Information Provider Layman"),
        smart_str(u"Information Provider Operator"),
        smart_str(u"Information Provider Expert"),
        smart_str(u"Mobile Context"),
        smart_str(u"Spatial Coordinates"),
        smart_str(u"Ask Questions"),
        smart_str(u"Give Suggestions"),
        smart_str(u"Rate or Comment"),
        smart_str(u"Create Personal Profile"),
        smart_str(u"Others Information Needs"),
        smart_str(u"Contact Other Users")
         ])
        i=0
        if(len(result_list)==len(url_list)==len(category_list)==len(website_list)):
            while operator.ne(i,len(result_list)) and operator.ne(i,len(url_list)) and operator.ne(i,len(category_list)) and \
                   operator.ne(i,len(website_list)):
                    """writer.writerow([
                    smart_str(url_list[i]),
                    smart_str(category_list[i]),
                    smart_str(dict_time_constraint.keys()[dict_time_constraint.values().index(result_list[i][0])]),
                    smart_str(dict_answer_validity.keys()[dict_answer_validity.values().index(result_list[i][1])]),
                    smart_str(dict_generality_applicability.keys()[dict_generality_applicability.values().index(result_list[i][2])]),
                    smart_str(dict_location_constraint.keys()[dict_location_constraint.values().index(result_list[i][3])]),
                    smart_str(dict_degree_knowledge.keys()[dict_degree_knowledge.values().index(result_list[i][4])])
                    ])"""
                    writer.writerow([
                    smart_str(website_list[i]),
                    smart_str(category_list[i]),
                    smart_str(url_list[i]),
                    smart_str(result_list[i][0]),
                    smart_str(result_list[i][1]),
                    smart_str(result_list[i][2]),
                    smart_str(result_list[i][3]),
                    smart_str(result_list[i][4]),
                    smart_str(result_list[i][5]),
                    smart_str(result_list[i][6]),
                    smart_str(result_list[i][7]),
                    smart_str(result_list[i][8]),
                    smart_str(result_list[i][9]),
                    smart_str(result_list[i][10]),
                    smart_str(result_list[i][11]),
                    smart_str(result_list[i][12]),
                    smart_str(result_list[i][13]),
                    smart_str(result_list[i][14]),
                    smart_str(result_list[i][15]),
                    smart_str(result_list[i][16]),
                    ])
                    i+=1
        else:
            pass
        return response
    aggregate_data.short_description = u"Export the aggregated data into a CSV file"

    def export_csv(modeladmin, request, queryset):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=aggregated_data.csv'
        writer = csv.writer(response, csv.excel)
        response.write(u'\ufeff'.encode('utf8')) # BOM (optional...Excel needs it to open UTF-8 file properly)
        writer.writerow([
        smart_str(u"Website"),
        smart_str(u"Category"),
        smart_str(u"Url"),
        smart_str(u"Time Constraint"),
        smart_str(u"Answer Validity"),
        smart_str(u"Generality Of Applicability"),
        smart_str(u"Location Dependency"),
        smart_str(u"Knowledge Codification"),
        smart_str(u"Costs Category"),
        smart_str(u"Information Provider Layman"),
        smart_str(u"Information Provider Operator"),
        smart_str(u"Information Provider Expert"),
        smart_str(u"Mobile Context"),
        smart_str(u"Spatial Coordinates"),
        smart_str(u"Ask Questions"),
        smart_str(u"Give Suggestions"),
        smart_str(u"Rate or Comment"),
        smart_str(u"Create Personal Profile"),
        smart_str(u"Others Information Needs"),
        smart_str(u"Contact Other Users")
        ])
        for obj in queryset:
            print obj.info_provider_operator
            writer.writerow([
                smart_str(obj.post_url.website.name),
                smart_str(obj.post_url.website.category),
                smart_str(obj.post_url),
                smart_str(obj.time_constraint),
                smart_str(obj.answer_validity),
                smart_str(obj.generality_applicability),
                smart_str(obj.location_constraint),
                smart_str(obj.degree_knowledge),
                smart_str(obj.costs_parameters),
                smart_str(obj.info_provider_layman),
                smart_str(obj.info_provider_operator),
                smart_str(obj.info_provider_expert),
                smart_str(obj.mobile_context),
                smart_str(obj.spatial_coordinates),
                smart_str(obj.ask_questions),
                smart_str(obj.suggestions),
                smart_str(obj.comment),
                smart_str(obj.personal_profile),
                smart_str(obj.others_information_need),
                smart_str(obj.contact_user),
                ])
        return response
    export_csv.short_description = u"Export the saved data into a CSV file"

    def export_time_statistics(modeladmin, request, queryset):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=time_statistics.csv'
        writer = csv.writer(response, csv.excel)
        response.write(u'\ufeff'.encode('utf8')) # BOM (optional...Excel needs it to open UTF-8 file properly)
        writer.writerow([
        smart_str(u"User ID"),
        smart_str(u"URL"),
        smart_str(u"Time Duration")
            ])
        for obj in queryset:
            writer.writerow([
                smart_str(obj.user_id),
                smart_str(obj.post_url),
                smart_str(obj.time_delta)
                ])

        return response
    export_time_statistics.short_description = u"Export the time statistics into a CSV file"

class CodeStatisticsAdmin(admin.ModelAdmin):
    # form = PostAdminForm
    list_filter = ['worker', 'completion_code']
    list_display = ['worker', 'completion_code']
    actions = ['export_code_statistics']

    def export_code_statistics(modeladmin, request, queryset):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=code_statistics.csv'
        writer = csv.writer(response, csv.excel)
        response.write(u'\ufeff'.encode('utf8')) # BOM (optional...Excel needs it to open UTF-8 file properly)
        writer.writerow([
        smart_str(u"Worker ID"),
        smart_str(u"Completion Code"),
            ])
        for obj in queryset:
            writer.writerow([
                smart_str(obj.worker),
                smart_str(obj.completion_code)
                ])

        return response
    export_code_statistics.short_description = u"Export the code statistics into a CSV file"

admin.site.register(Website, WebsiteAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(WebsiteEvaluation, WebsiteEvaluationAdmin)
admin.site.register(CodeStatistics, CodeStatisticsAdmin)