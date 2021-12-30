# -*- coding: utf-8 -*-

from django.contrib import admin

from dj_beneficiary.models import Agent, FacilityType, Facility, ImplementingPartner


@admin.register(Agent)
class AgentAdmin(admin.ModelAdmin):
    pass


@admin.register(FacilityType)
class FacilityTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(Facility)
class FacilityAdmin(admin.ModelAdmin):
    pass


@admin.register(ImplementingPartner)
class ImplementingPartnerAdmin(admin.ModelAdmin):
    pass
