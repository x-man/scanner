# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from InfoCollector.models import Domain, SubDomain, Ip
from subDomainBrute.subDomainsBrute import SubNameBrute, Option
import re, requests, bs4
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
	domain = get_object_or_404(Domain, pk=id)
	domain.status = 2
	domain.save()
	options = Option()
	d = SubNameBrute(domain.domain, options=options)
	d.run()
	d.outfile.flush()
	d.outfile.close()
	subDomainFile  = d.output
	with open('subDomainFile') as fr:
		regex = re.compile('[\s,]+')
		for line in fr:
			line = line.strip()
			subDomains = regex.split(line)
			subdomain = subDomains[0]
			html = requests.get('http://'+subdomain).content
			html = bs4.BeautifulSoup(html)
			subdomain = domain.subDomain_set.create(subdomain=subdomain,title=html.title.text,add_date=timezone.now())

			for ip in subDomains[1:]:
				subdomain.ip_set.create(ip=ip, date=timezone.now())
	domain.status = 3
	domain.save()
	


