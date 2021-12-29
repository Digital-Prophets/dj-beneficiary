# -*- coding: utf-8 -*-

import datetime
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from imagekit.processors import ResizeToFill
from imagekit.models import ProcessedImageField


class Province(models.Model):
    """
    Implements province properties and appropriate methods.
    """

    name = models.CharField(_("Province"), max_length=255)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Province"
        verbose_name_plural = "Provinces"
        ordering = ["-created"]

class District(models.Model):
    """
    Define district properties and appropriate methods.
    """

    name = models.CharField(
        _("District"),
        max_length=255
    )
    province = models.ForeignKey(
        Province,
        on_delete=models.CASCADE,
    )
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Ward(models.Model):
    """
    Defines a Ward and all its approriate implemeentation methods.
    """

    name = models.CharField(
        _("District"),
        max_length=255
    )

    district = models.ForeignKey(
        District,
        on_delete=models.CASCADE,
    )

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

NGO = 1
COMPANY = 2
GOVERNMENT = 3
OTHER = 4
IP_TYPES = (
    (NGO, _('Non-Profit Organization')),
    (COMPANY, _('Company')),
    (GOVERNMENT, _('Government')),
    (OTHER, _('Other')),
)
class ImplementingPartner(models.Model):
    name = models.CharField(
        _('Name'),
        max_length=200,
    )

    ip_type = models.IntegerField(
        _('Type'),
        choices=IP_TYPES,
        default=NGO,
    )

    is_active = models.BooleanField(
        _('Is Active'),
        default=True,
        help_text=_('Is still an active Implementing Partner'),
    )

    def __str__(self):
        return self.name

class FacilityType(models.Model):
    name = models.CharField(
        _('Facility Type Name'),
        max_length=200,
    )

    def __str__(self):
        return self.name.title()

class Facility(models.Model):
    hmis_code = models.CharField(
        _('HMIS Code'),
        max_length=100,
        null=True,
        blank=True
    )
    district = models.ForeignKey(
        District,
        default=1,
        on_delete=models.CASCADE,
        help_text=_("District in which the facility is located"),
        max_length=250,
    )
    name = models.CharField(
        _('Name'),
        max_length=200,
        help_text=_(
            "Just enter name without 'Hostpial' or 'Clinic`, i.e for `Kitwe General Hospital` just enter `Kitwe General`.")
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

    class Meta:
        verbose_name = 'Facility'
        verbose_name_plural = 'Facilities'

    def save(self):
        if self.facility_type.name.lower() in self.name.lower():
            self.name = (self.name).title()
        else:
            f"{self.name.title()} {self.facility_type.name.title()}"
        super(Facility, self).save()

    def __str__(self):
        return str(self.name)


GENDER_CHOICES = (
    ("Male", _("Male")),
    ("Female", _("Female")),
    ("Transgender", _("Transgender")),
    ("Other", _("Other"))
)
SEX_CHOICES = (
    ("Male", _("Male")),
    ("Female", _("Female"))
)

class Agent(models.Model):
    """
    Create agent detail table with its attributes or columns.
    """
    first_name = models.CharField(
        _("First Name"),
        max_length=200,
        null=True,
        blank=True
    )
    last_name = models.CharField(
        _("Last Name"),
        max_length=200,
        null=False
    )
    birthdate = models.DateField(
        _("Birth Date"),
        auto_now_add=False,
        null=True,
        blank=True
    )
    agent_id = models.CharField(
        max_length=100,
        editable=False
    )
    gender = models.CharField(
        _("Gender"),
        max_length=50,
        choices=GENDER_CHOICES,
        default=GENDER_CHOICES[3][0]
    )
    # location = models.PointField(
    #     _("Location"),
    #     geography=True,
    #     blank=True,
    #     null=True,
    #     srid=4326
    # )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class IndividualBeneficiary(models.Model):
    """
    Implements the Beneficiary object as an individual Person.
    """
    ART_STATUS_CHOICES = (
        ("Enrolled", _("Enrolled")),
        ("Not Enrolled", _("Not Enrolled")),
    )
    HIV_STATUS_CHOICES = (
        ("Positive", _("Positive")),
        ("Negative", _("Negative")),
    )

    MARITAL_STATUS = (
        ("single", _("Single")),
        ("married", _("Married")),
        ("seperated", _("Seperated")),
        ("divorced", _("Divorced")),
        ("widowed", _("Widowed")),
    )

    HIV_STATUS = (
        ("positive", _("Positive")),
        ("negative", _("Negative")),
        ("unkown", _("Uknown")),
    )

    EDUCATION_LEVEL = (
        ("none", _("None")),
        ("primary", _("Primary")),
        ("basic", _("Basic")),
        ("secondary", _("Secondary O'Level")),
        ("certificate", _("Certificate")),
        ("diploma", _("Diploma")),
        ("degree", _("Degree")),
        ("masters", _("Masters")),
        ("doctrate", _("Doctrate")),
        ("phd", _("PHD")),
    )

    first_name = models.CharField(
        _("First Name"),
        max_length=200
    )
    last_name = models.CharField(
        _("Last Name"),
        max_length=200
    )
    other_name = models.CharField(
        _("Other Name"),
        max_length=200,
        null=True,
        blank=True
    )
    gender = models.CharField(
        _("Gender"),
        max_length=100,
        choices=GENDER_CHOICES,
        default=GENDER_CHOICES[3][0]
    )
    sex = models.CharField(
        _("Sex"),
        max_length=100,
        choices=SEX_CHOICES
    )
    profile_photo = ProcessedImageField(
        upload_to='profile_photo',
        processors=[ResizeToFill(512, 512)],
        format='JPEG',
        options={'quality': 100},
        null=True,
        blank=True
    )
    phone_number = models.CharField(
        _("Phone Number"),
        max_length=20,
        null=True,
        blank=True
    )
    email = models.EmailField(
        _("Email"),
        max_length=200,
        null=True,
        blank=True
    )
    beneficiary_id = models.CharField(
        max_length=100,
        editable=False
    )
    art_status = models.CharField(
        _("ART Status"),
        max_length=100,
        choices=ART_STATUS_CHOICES,
        null=True,
        blank=True
    )
    last_vl = models.IntegerField(
        _("Last Viral Load"),
        null=True,
        blank=True
    )
    hiv_status = models.CharField(
        _("HIV Status"),
        choices=HIV_STATUS,
        max_length=100,
        null=True,
        blank=True,
    )
    agent = models.ForeignKey(
        Agent,
        on_delete=models.PROTECT,
        null=True,
        blank=True
    )
    registered_facility = models.ForeignKey(
        'Facility',
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="registerd_facility"
    )
    date_of_birth = models.DateField(_("Date of Birth"))
    marital_status = models.CharField(
        _("Marital Status"),
        choices=MARITAL_STATUS,
        max_length=100,
        null=True,
        blank=True
    )
    name_of_spouse = models.CharField(
        _("Phone Number"),
        max_length=200,
        null=True,
        blank=True
    )
    number_of_children = models.IntegerField(
        _("Number of children"),
        null=True,
        blank=True
    )
    number_of_siblings = models.IntegerField(
        _("Number of siblings"),
        null=True,
        blank=True
    )
    education_level = models.CharField(
        _("Education level"),
        max_length=300,
        null=True,
        blank=True,
        choices=EDUCATION_LEVEL
    )
    address = models.TextField(
        _("Address"),
        null=True,
        blank=True,
    )
    alive = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = "Beneficiary Person"
        verbose_name_plural = "Beneficiary Persons"
        ordering = ["created"]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_age(self):
        """
        Calculates the Beneficiaries age from birth date.
        """
        days_in_year = 365.2425
        age = int((datetime.date.today() - self.date_of_birth).days / days_in_year)
        return age


class OrganizationBeneficiary(models.Model):
    """
    Implements the Beneficiary object an organizational entity.
    i.e co-oroperative, business firm etc.
    """

    BENEFICIARY_ORGANIZATION_TYPE = (
        ("coorperative", _("Co-orperative")),
        ("businessfirm", _("Business Firm")),
        ("Other", _("Other")),
    )

    name = models.CharField(
        _("Organization Name"),
        max_length=200
    )
    org_type = models.CharField(
        _("Organization Type"),
        max_length=100,
        choices=BENEFICIARY_ORGANIZATION_TYPE,
    )
    ward = models.ForeignKey(
        Ward, 
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    logo = ProcessedImageField(
        upload_to='org_logos',
        processors=[ResizeToFill(512, 512)],
        format='JPEG',
        options={'quality': 100},
        null=True,
        blank=True
    )
    total_beneficiaries = models.IntegerField(
        _("Total Individual Beneficiary Count"),
        null=True, 
        blank=True
    )
    total_females = models.IntegerField(
        _("Total Female Count"),
        null=True, 
        blank=True
    )
    total_males = models.IntegerField(
        _("Total Male Count"),
        null=True, 
        blank=True
    )
    total_hhs = models.IntegerField(
        _("Total HHs"),
        null=True, 
        blank=True
    )
    female_hhs = models.IntegerField(
        _("Female HHs"),
        null=True, 
        blank=True
    )
    below_sixteen = models.IntegerField(
        _("Below 16 Years Old"),
        null=True, 
        blank=True
    )
    sixteen_to_thirty = models.IntegerField(
        _("16 to 30 Years Old"),
        null=True, 
        blank=True
    )
    thirty_to_fourty_five = models.IntegerField(
        _("30 to 40 Years Old"),
        null=True, 
        blank=True
    )
    above_fourty_five = models.IntegerField(
        _("Above 40 Years Old"),
        null=True, 
        blank=True
    )

    description = models.TextField(
        _("Description"),
        null=True,
        blank=True
    )
    email = models.EmailField(
        _("Email"),
        max_length=200,
        null=True,
        blank=True
    )
    cell = models.CharField(
        _("Phone Number"),
        max_length=100,
        null=True,
        blank=True
    )
    registered_date = models.DateField(
        null=True,
        blank=True,
    )
    created = models.DateTimeField(auto_now_add=True)
    class Meta:
        # NOTE: This means we can not reuse this model directly but subclass it with inheritance and add extra fields or override existing fields
        abstract = True 
        verbose_name = "Beneficiary Organization"
        verbose_name_plural = "Beneficiary Organizations"
        ordering = ["created"]

    def __str__(self):
        return f"{self.name}"

