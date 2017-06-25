# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from InfoCollector.models import Domain, SubDomain, Ip, WebFingerprint
from .tasks import brute, scan_subdomain
# Create your views here.
def index(request):
	return render(request, 'infocollector/index.html')

def collect(request):
	if 'domain' in request.POST:
		domain = request.POST['domain']
		company = request.POST['company'] if 'company' in request.POST else ''
		d = Domain(domain=domain, company=company, add_date=timezone.now())
		d.save()
	domains = Domain.objects.all()
	context = {'domains':domains}
	return render(request, 'infocollector/domain.html', context)

def deleteDomain(request,id):
	domain = get_object_or_404(Domain, pk=id)
	domain.delete()
	domains = Domain.objects.all()
	context = {'domains':domains}
	return render(request, 'infocollector/domain.html', context)

def subDomainBrute(request,id):
	domain.status = 2
	domain.save()
	brute.delay(id)

	domains = Domain.objects.all()
	context = {'domains':domains}
	return render(request, 'infocollector/domain.html', context)

def show(request,param):
	if param == 'domain':
		domains = Domain.objects.all()
		context = {'domains':domains}
	elif param == 'subdomain':
		subdomains = SubDomain.objects.all()
		context = {'subdomains':subdomains}
	elif param == 'ip':
		ips = Ip.objects.all()
		context = {'ips':ips}
	elif param == 'port':
		pass
	elif param == 'vuln':
		pass
	elif param == 'webfingerprint':
		webfinerprints = WebFingerprint.objects.all()
		context = {'webfinerprints':webfinerprints}
	return render(request, 'infocollector/domain.html', context)

def subDomainScan(request,id):
	subdomain.status = 2
	subdomain.save()
	scan_subdomain.delay(id)

	subdomains = SubDomain.objects.all()
	context = {'subdomains':subdomains}
	return render(request, 'infocollector/domain.html', context)
