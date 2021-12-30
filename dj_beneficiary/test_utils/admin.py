from django.contrib import admin
from django.contrib import admin

# Put your models admin models here
from dj_beneficiary.test_utils.models import (
    District,
    IndividualBeneficiary,
    Beneficiary,
    Province,
    Ward,
)


@admin.register(IndividualBeneficiary)
class IndividualBeneficiaryAdmin(admin.ModelAdmin):
    pass


@admin.register(Beneficiary)
class BeneficiaryAdmin(admin.ModelAdmin):
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
