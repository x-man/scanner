# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils import timezone
from django.shortcuts import render
from InfoCollector.models import Domain
# Create your views here.
def index(request):
    return render(request, 'infocollector/index.html')

def collect(request):
    if 'domain' in request.POST:
        domain = request.POST['domain']
        d = Domain(domain=domain, company='', add_date=timezone.now())
        d.save()
    domains = Domain.objects.all()
    context = {'domains':domains}
    return render(request, 'infocollector/domain.html', context)