from django.db import models
from django.utils.translation import gettext_lazy as _

from dj_beneficiary.models import (
    AbstractDistrict,
    BaseIndividualBeneficiaryAbstract,
    BaseOrganizationBeneficiaryAbstract,
    AbstractProvince,
    AbstractWard,
    Facility,
)


# Put your test models here
class Province(AbstractProvince):
    pass


class District(AbstractDistrict):
    province = models.ForeignKey(
        Province,
        on_delete=models.CASCADE,
    )


class Ward(AbstractWard):
    district = models.ForeignKey(
        District,
        on_delete=models.CASCADE,
    )

class IndividualBeneficiary(BaseIndividualBeneficiaryAbstract):
    registered_facility = models.ForeignKey(
        Facility,
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