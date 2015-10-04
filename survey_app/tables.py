import django_tables2 as tables
from .models import WebsiteEvaluation
from django.utils.translation import gettext_lazy as _
from .models import WebsiteEvaluation,Post

class WebsiteEvaluationTable(tables.Table):
    url = tables.URLColumn(verbose_name=_('Url Analyzed'))
    rated = tables.TemplateColumn('{{ record.get_url_count }}', verbose_name=_('Times Rated'))
    time_taken = tables.TemplateColumn('{{ record.get_time_delta }}', verbose_name=_('Time in Minutes'))

    class Meta:
        model = Post
        orderable = False
        attrs = {'class': 'table table-striped  table-bordered table-hover table-condensed paleblue'}
        sequence = ['url', 'rated', 'time_taken']
        fields = ['url']


class CodeStatisticsTable(tables.Table):
    worker = tables.Column(verbose_name=_('User ID'))
    completion_code = tables.Column(verbose_name=_('Code to be shown'))

    class Meta:
        model = WebsiteEvaluation
        orderable = False
        attrs = {'class': 'table table-striped  table-bordered table-hover table-condensed paleblue'}
        sequence = ['worker', 'completion_code']
        fields = ['worker', 'completion_code']