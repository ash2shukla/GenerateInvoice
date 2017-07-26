# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class database(models.Model):
    firm = models.CharField(max_length=500,null=True)
    bill_type = modles.CharField(max_length=500,null=True)
    invoice_no = models.CharField(max_length=500,null=True)
    dated =  models.CharField(max_length=500,null=True)
    party_details = models.CharField(max_length=500,null=True)
    party_tin = models.CharField(max_length=500,null=True)
    transport = models.CharField(max_length=500,null=True)
    station = models.CharField(max_length=500,null=True)
    vehicle_no = models.CharField(max_length=500,null=True)
    desc = models.CharField(max_length=5000,null=True)
    qty = models.CharField(max_length=500,null=True)
    unit = models.CharField(max_length=500,null=True)
    price = models.CharField(max_length=500,null=True)
    gst = models.CharField(max_length=500,null=True)
