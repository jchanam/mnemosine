# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Season, PaymentType, Payment


admin.site.register(Season)
admin.site.register(PaymentType)
admin.site.register(Payment)
