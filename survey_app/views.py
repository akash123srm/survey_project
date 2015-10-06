import random
import string
import math
from time import strftime, gmtime,strptime
import datetime
from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseNotFound
from .forms import EvaluationForm
from .models import WebsiteEvaluation,Post
from .models import *
from django.core.urlresolvers import reverse
from django.utils import formats, timezone
from sets import Set
from .tables import WebsiteEvaluationTable,CodeStatisticsTable
from django_tables2   import RequestConfig
from django.views.generic.base import TemplateView
from django.contrib import messages
# Create your views here.

class LandingView(TemplateView):
    template_name="landing.html"

    def get_context_data(self, **kwargs):
        pass


def survey_view(request):
    #sets the expiry date of a session in future

    request.session.set_expiry(timezone.now() + datetime.timedelta(days=365))
    if request.session._session_key:
        USER_ID = request.session._session_key
    else:
        USER_ID = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(32))

    time_value = datetime.time(hour=datetime.datetime.now().hour, minute=datetime.datetime.now().minute, second=datetime.datetime.now().second)

    if request.method == 'POST':
       form = EvaluationForm(request.POST)
       if form.is_valid():
               time_shown = strptime(request.POST['time_value'], '%H:%M:%S')
               duration_minutes = round(float((datetime.timedelta(hours=time_value.hour, minutes=time_value.minute, seconds=time_value.second)-\
                   datetime.timedelta(hours=time_shown.tm_hour, minutes=time_shown.tm_min, seconds=time_shown.tm_sec)).seconds)/60,2)
               print duration_minutes
               p, created = Post.objects.get_or_create(url=request.POST['url'])
               p.save()
               evaluation,created = WebsiteEvaluation.objects.get_or_create(user_id=USER_ID, post_url=p,
                                                    time_constraint = form.cleaned_data['time_constraint'],
                                                    answer_validity = form.cleaned_data['answer_validity'],
                                                    generality_applicability=form.cleaned_data['generality_applicability'],
                                                    location_constraint=form.cleaned_data['location_constraint'],
                                                    degree_knowledge=form.cleaned_data['degree_knowledge'],
                                                    costs_parameters=form.cleaned_data['costs_parameters'],
                                                    info_need_identification=form.cleaned_data['info_need_identification'],
                                                    info_provider_layman=form.cleaned_data['info_provider_layman'],
                                                    info_provider_operator=form.cleaned_data['info_provider_operator'],
                                                    info_provider_expert=form.cleaned_data['info_provider_expert'],
                                                    mobile_context=form.cleaned_data['mobile_context'],
                                                    spatial_coordinates=form.cleaned_data['spatial_coordinates'],
                                                    ask_questions=form.cleaned_data['ask_questions'],
                                                    suggestions=form.cleaned_data['suggestions'],
                                                    comment=form.cleaned_data['comment'],
                                                    personal_profile=form.cleaned_data['personal_profile'],
                                                    others_information_need=form.cleaned_data['others_information_need'],
                                                    contact_user=form.cleaned_data['contact_user'],
                                                    time_delta=duration_minutes
                                                    )
               evaluation.save()
               return HttpResponseRedirect(reverse('survey_view'))
    else:
        form = EvaluationForm()
    posts = [p for p in Post.objects.all()]
    posts_evaluated = [p.post_url for p in WebsiteEvaluation.objects.all()]
    posts_evaluated_per_user = [p.post_url for p in WebsiteEvaluation.objects.filter(user_id=USER_ID)]
    #print posts
    #print posts_evaluated
    posts_random = list(Set(posts).difference(Set(posts_evaluated)))

    if len(posts_evaluated_per_user) >= 3:
        success_code = ''.join(random.choice(string.ascii_uppercase) for _ in range(3)) + \
                       ''.join(random.choice(string.digits) for _ in range(3))
        try:
            obj = CodeStatistics.objects.get(worker=USER_ID)


        except CodeStatistics.DoesNotExist:
            obj = None
            c, created = CodeStatistics.objects.get_or_create(worker=USER_ID, completion_code=success_code)
            c.save()
        return render(request, 'success_code.html', {'success_code': success_code})

    else:

        url = random.choice(posts_random)
        return render(request, 'survey_form.html', {'form': form,
                                                    'url': url,
                                                    'evaluation_count': len(posts_evaluated_per_user),
                                                    'total_count': 3,
                                                    'time_value': time_value}
                                                                            )




class SuccessView(TemplateView):
    template_name="success.html"

    def get_context_data(self, **kwargs):
        pass

class StatisticsView(TemplateView):
    template_name = "statistics.html"

    def get_context_data(self, **kwargs):
        objects = set([w.post_url for w in WebsiteEvaluation.objects.all()])
        evaluation_table = WebsiteEvaluationTable(objects)
        RequestConfig(self.request).configure(evaluation_table)
        p_evaluated = WebsiteEvaluation.objects.all()
        if len(p_evaluated):
            self.average_time_delta = (sum([t.time_delta for t in WebsiteEvaluation.objects.all()]))/len(p_evaluated)
        return {'evaluation_table': evaluation_table,
                'average_time': round(self.average_time_delta, 2)}


class StatisticsCodeView(TemplateView):
    template_name = "statistics_code.html"

    def get_context_data(self, **kwargs):
        code_statistics_table = CodeStatisticsTable(CodeStatistics.objects.all())
        RequestConfig(self.request).configure(code_statistics_table)
        return {'code_statistics_table': code_statistics_table
               }


class SuccessCodeView(TemplateView):
    template_name = "success_code.html"

    def get_context_data(self, **kwargs):
        pass

from reportlab.pdfgen import canvas
from django.http import HttpResponse

def download_success_code_view(request,code):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment;filename = "code.pdf"'
    p  = canvas.Canvas(response)
    p.drawString(100,100,code)
    p.showPage()
    p.save()
    return response