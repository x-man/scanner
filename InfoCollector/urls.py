from django.conf.urls import url
from .import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^collect$', views.collect, name='collect'),
    url(r'^deleteDomain/(?P<id>[0-9]+)$', views.deleteDomain, name='deleteDomain'),
    url(r'^subDomainBrute/(?P<id>[0-9]+)$', views.subDomainBrute, name='subDomainBrute'),
    url(r'^show/(?P<param>(domain|subdomain|ip|port|vuln|webfingerprint))$', views.show, name='show'),
    url(r'^subDomainScan/(?P<id>[0-9]+)$', views.subDomainScan, name='subDomainScan'),
    url(r'^addWebFingerprint$', views.addWebFingerprint, name='addWebFingerprint'),
    url(r'^deleteWebFingerprint/(?P<id>[0-9]+)$', views.deleteWebFingerprint, name='deleteWebFingerprint'),
]