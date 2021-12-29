# -*- coding: utf-8 -*-

from django.contrib import admin

from .models import (
   IndividualBeneficiary,
   Facility,
   Province,
   District,
   Ward,
)


@admin.register(IndividualBeneficiary)
class IndividualBeneficiaryAdmin(admin.ModelAdmin):
    pass

# @admin.register(OrganizationBeneficiary)
# class OrganizationBeneficiaryAdmin(admin.ModelAdmin):
#     pass

@admin.register(Facility)
class FacilityAdmin(admin.ModelAdmin):
    pass


@admin.register(Province)
class ProvinceAdmin(admin.ModelAdmin):
    pass


@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    pass


@admin.register(Ward)
class WardAdmin(admin.ModelAdmin):
    pass



