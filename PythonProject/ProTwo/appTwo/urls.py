from django.conf.urls import url, include
from appTwo import views

app_name = "appTwo"

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^(?P<question_id>[0-9]+)/$',views.detail,name='detail'),
    url(r'^(?P<question_id>[0-9]+)/results$',views.results,name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote$',views.vote,name='vote'),
    url(r'^login/$', views.login, name='login'),
    url(r'^about/$', views.about, name='about'),
    url(r'^placements/$', views.placements, name='placements'),
    url(r'^admissions/$', views.admissions, name='admissions'),
]
