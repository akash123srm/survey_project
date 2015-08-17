from django.conf.urls import patterns, url
from survey_app import views

urlpatterns = patterns('',
    url(r'^$', views.survey_view, name='survey_view'),
    url(r'^success$', views.SuccessView.as_view(),name='success_view'),
    url(r'^statistics$', views.StatisticsView.as_view(), name='statistics_view'),
    url(r'^evaluation_complete$', views.EvaluationCompleteView.as_view(), name='evaluation_complete_view'),
)
