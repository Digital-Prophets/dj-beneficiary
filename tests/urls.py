# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.urls import path, include
from django.contrib import admin

app_name = 'dj-beneficiary'

urlpatterns = [
    path('admin/', admin.site.urls, name='dj-beneficiary-admin'),
    path('', include('dj_beneficiary.urls', namespace='beneficiary')),
]
