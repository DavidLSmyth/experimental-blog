from django.conf.urls import url, include

from . import views
app_name='polls'
urlpatterns = [
    url(r'^$', views.polls, name='polls'),
    url(r'^(1)$', views.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^/(1)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    url(r'^/(1)/vote/$', views.vote, name='vote'),
]
