from django.conf.urls import url
from .import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^collect$', views.collect, name='collect'),
    url(r'^deleteDomain/(?P<id>[0-9]+)$', views.deleteDomain, name='deleteDomain'),
    url(r'^subDomainBrute/(?P<id>[0-9]+)$', views.subDomainBrute, name='subDomainBrute'),
]