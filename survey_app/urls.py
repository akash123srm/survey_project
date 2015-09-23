from django.conf.urls import patterns, url
from survey_app import views

urlpatterns = patterns('',
    url(r'^$', views.LandingView.as_view(), name='landing_view'),
    url(r'^survey_form', views.survey_view, name='survey_view'),
    url(r'^success$', views.SuccessView.as_view(),name='success_view'),
    url(r'^statistics$', views.StatisticsView.as_view(), name='statistics_view'),
    url(r'^success_code$', views.SuccessCodeView.as_view(), name='success_code_view'),
)
