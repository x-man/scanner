# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Domain(models.Model):
    'table domain'
    domain = models.CharField(max_length=50)
    company = models.CharField(max_length=50,null=True)
    add_date = models.DateTimeField('date add')
    status = models.IntegerField(default=1, null=True)

class SubDomain(models.Model):
    'table subdomain'
    subdomain = models.CharField(max_length=50)
    title = models.CharField(max_length=50,null=True)
    server = models.CharField(max_length=50,null=True)
    # server_version = models.CharField(max_length=50,null=True)
    dev_language = models.CharField(max_length=50,null=True)
    # language_version = models.CharField(max_length=50,null=True)
    cms = models.CharField(max_length=50,null=True)
    # cms_version = models.CharField(max_length=50,null=True)
    add_date = models.DateTimeField('date add')
    domain = models.ForeignKey(Domain)
    status = models.IntegerField(default=1, null=True)
    is_access = models.IntegerField(default=0, null=True)

class Ip(models.Model):
    'table ip'
    ip = models.CharField(max_length=50)
    is_intranet = models.IntegerField(default=0,null=True)
    position = models.CharField(max_length=100,null=True)
    date = models.DateTimeField('add date')
    subdomain = models.ForeignKey(SubDomain)
    status = models.IntegerField(default=1, null=True)

class WebFingerprint(models.Model):
    'table web fingerprint'
    app = models.CharField(max_length=50)
    app_description = models.CharField(max_length=50,null=True)
    rule = models.CharField(max_length=200,null=True)