from django.contrib.admin import AdminSite
from django.contrib.sites.models import Site
from django_tables2.config import RequestConfig
from survey_app.models import WebsiteEvaluation
#from survey_app.tables import WebsiteEvaluationTable

"""class SurveyAdminSite(AdminSite):
    def index(self, request, extra_context=None):
        if extra_context is None:
            extra_context = {}

        evaluation_table = WebsiteEvaluationTable(WebsiteEvaluation.objects.all(),
            page_field='page_evaluation'
        )
        RequestConfig(request, paginate={"per_page": 10}).configure(evaluation_table)

        index_context = {
            'evaluation_table': evaluation_table,
            'is_index': True,
        }
        extra_context.update(index_context)
        return super().index(request, extra_context)

survey_site = SurveyAdminSite()
survey_site.register(Site)"""
