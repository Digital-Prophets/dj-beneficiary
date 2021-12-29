from django.contrib import admin

# Put your models admin models here
from dj_beneficiary.test_utils.models import (
    Agent,
    District,
    Facility,
    IndividualBeneficiary,
    OrganizationBeneficiary,
    Province,
    Ward,
)


# -*- coding: utf-8 -*-

from django.contrib import admin

from .models import (
    IndividualBeneficiary,
    ImplementingPartner,
    FacilityType,
    Facility,
    Province,
    District,
    Ward,
)


@admin.register(Agent)
class AgentAdmin(admin.ModelAdmin):
    pass


@admin.register(IndividualBeneficiary)
class IndividualBeneficiaryAdmin(admin.ModelAdmin):
    pass


@admin.register(OrganizationBeneficiary)
class OrganizationBeneficiaryAdmin(admin.ModelAdmin):
    pass


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


@admin.register(ImplementingPartner)
class ImplementingPartnerAdmin(admin.ModelAdmin):
    pass


@admin.register(FacilityType)
class FacilityTypeAdmin(admin.ModelAdmin):
    pass
