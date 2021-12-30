from django.db import models
from django.utils.translation import gettext_lazy as _

from dj_beneficiary.models import (
    AbstractLocation,
    AbstractIndividualBeneficiary,
    AbstractOrganizationBeneficiary,
    Facility,
)


# Put your test models here
class Province(AbstractLocation):
    class Meta:
        abstract = False
        verbose_name = "Province"
        verbose_name_plural = "Provinces"
        ordering = ["-created"]


class District(AbstractLocation):
    province = models.ForeignKey(
        Province,
        on_delete=models.CASCADE,
    )
    class Meta:
        abstract = False
        verbose_name = "District"
        verbose_name_plural = "Districts"
        ordering = ["-created"]

District._meta.get_field('name').verbose_name = 'District name'
District._meta.get_field('name').help_text = 'The name of the District.'

class Ward(AbstractLocation):
    district = models.ForeignKey(
        District,
        on_delete=models.CASCADE,
    )
    class Meta:
        abstract = False
        verbose_name = "Ward"
        verbose_name_plural = "Wards"
        ordering = ["-created"]

class IndividualBeneficiary(AbstractIndividualBeneficiary):
    registered_facility = models.ForeignKey(
        Facility,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="registerd_facility"
    )


class Beneficiary(AbstractOrganizationBeneficiary):
    ward = models.ForeignKey(
        Ward, 
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    class Meta:
        abstract = False
        verbose_name = "Beneficiary Organization"
        verbose_name_plural = "Beneficiary Organizations"
