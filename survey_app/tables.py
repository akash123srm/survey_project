import django_tables2 as tables
from .models import WebsiteEvaluation
from django.utils.translation import gettext_lazy as _
from .models import WebsiteEvaluation,Post

class WebsiteEvaluationTable(tables.Table):
    url = tables.URLColumn(verbose_name=_('Url Analyzed'))
   # no_users = tables.TemplateColumn('{{ record.get_user_count }}', verbose_name=_('No of Users'))
    rated = tables.TemplateColumn('{{ record.get_url_count }}', verbose_name=_('Times Rated'))

    class Meta:
        model = Post
        orderable = False
        attrs = {'class': 'table table-striped  table-bordered table-hover table-condensed paleblue'}
        sequence = ['url', 'rated']
        fields = ['url']


