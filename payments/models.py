# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings


AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')


class Season(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    description = models.CharField(max_length=50)

    def __unicode__(self):
        return self.description


class PaymentType(models.Model):
    description = models.CharField(max_length=255)
    quantity = models.FloatField()

    def __unicode__(self):
        return self.description


class Payment(models.Model):
    season = models.ForeignKey(Season)
    paymentType = models.ForeignKey(PaymentType)
    user = models.ForeignKey(AUTH_USER_MODEL)
    date = models.DateTimeField()
    paid = models.BooleanField()
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.season + " " + self.date + " " + self.user.verbose_name
