from django.db import models
from django.utils.translation import gettext_lazy as _

from dj_beneficiary.models import (
    BaseAgentAbstract,
    BaseDistrictAbstract,
    BaseFacilityAbstract,
    BaseIndividualBeneficiaryAbstract,
    BaseOrganizationBeneficiaryAbstract,
    BaseProvinceAbstract,
    BaseWardAbstract,
    ImplementingPartner,
    FacilityType
)


# Put your test models here
class Province(BaseProvinceAbstract):
    pass


class District(BaseDistrictAbstract):
    province = models.ForeignKey(
        Province,
        on_delete=models.CASCADE,
    )


class Ward(BaseWardAbstract):
    district = models.ForeignKey(
        District,
        on_delete=models.CASCADE,
    )


class Facility(BaseFacilityAbstract):
    district = models.ForeignKey(
        District,
        default=1,
        on_delete=models.CASCADE,
        help_text=_("District in which the facility is located"),
        max_length=250,
    )
    facility_type = models.ForeignKey(
        FacilityType,
        default=1,
        on_delete=models.CASCADE,
        help_text=_("Facility Type, i.e 'Hospital, Clinic etc"),
        max_length=250,
    )
    implementing_partner = models.ForeignKey(
        ImplementingPartner,
        on_delete=models.SET_NULL,
        help_text=_("Related Implementing Partner."),
        max_length=250,
        null=True,
        blank=True
    )


class Agent(BaseAgentAbstract):
    pass


class IndividualBeneficiary(BaseIndividualBeneficiaryAbstract):
    registered_facility = models.ForeignKey(
        'Facility',
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="registerd_facility"
    )


class OrganizationBeneficiary(BaseOrganizationBeneficiaryAbstract):
    ward = models.ForeignKey(
        Ward, 
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )