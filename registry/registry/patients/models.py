import copy
from django.db import models
from django.db.models.signals import post_save, pre_delete

import registry.groups.models

import logging
logger = logging.getLogger('patient')

from registry.utils import stripspaces
from django.conf import settings # for APP_NAME

class Country(models.Model):
    name = models.CharField(max_length=50, primary_key=True)

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "countries"

    def __unicode__(self):
        return self.name


class State(models.Model):
    short_name = models.CharField(max_length=3, primary_key=True)
    name = models.CharField(max_length=30)
    country = models.ForeignKey(Country)

    class Meta:
        ordering = ["country__name", "name"]

    def __unicode__(self):
        return self.name


class Doctor(models.Model):
    # TODO: Is it possible for one doctor to work with multiple working groups?
    family_name = models.CharField(max_length=100, db_index=True)
    given_names = models.CharField(max_length=100, db_index=True)
    surgery_name = models.CharField(max_length=100, blank=True)
    speciality = models.CharField(max_length=100)
    address = models.TextField()
    suburb = models.CharField(max_length=50, verbose_name="Suburb/Town")
    state = models.ForeignKey(State, verbose_name="State/Province/Territory")
    phone = models.CharField(max_length=30, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    def __unicode__(self):
        return "%s %s" % (self.family_name.upper(), self.given_names)

class NextOfKinRelationship(models.Model):
    relationship = models.CharField(max_length=100, verbose_name="Relationship")
    
    class Meta:
        verbose_name = 'Next of Kin Relationship'
    
    def __unicode__(self):
        return self.relationship

class Patient(models.Model):
    if settings.INSTALL_NAME == 'dm1':   # Trac #16 item 9
        SEX_CHOICES = ( ("M", "Male"), ("F", "Female") )
    else:
        SEX_CHOICES = ( ("M", "Male"), ("F", "Female"), ("X", "Other/Intersex") )

    working_group = models.ForeignKey(registry.groups.models.WorkingGroup, null=False, blank=False)
    consent = models.BooleanField(null=False, blank=False, help_text="Consent must be given for the patient to be entered on the registry", verbose_name="consent given")
    family_name = models.CharField(max_length=100, db_index=True)
    given_names = models.CharField(max_length=100, db_index=True)
    date_of_birth = models.DateField()
    place_of_birth = models.CharField(max_length=100, null=True, blank=True, verbose_name="Place of Birth")
    sex = models.CharField(max_length=1, choices=SEX_CHOICES)
    address = models.TextField()
    suburb = models.CharField(max_length=50, verbose_name="Suburb/Town")
    state = models.ForeignKey(State, verbose_name="State/Province/Territory", related_name="patient_set")
    postcode = models.IntegerField()
    home_phone = models.CharField(max_length=30, blank=True, null=True)
    mobile_phone = models.CharField(max_length=30, blank=True, null=True)
    work_phone = models.CharField(max_length=30, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    next_of_kin_family_name = models.CharField(max_length=100, verbose_name="family name")
    next_of_kin_given_names = models.CharField(max_length=100, verbose_name="given names")
    next_of_kin_relationship = models.ForeignKey(NextOfKinRelationship, verbose_name="Relationship", blank=True, null=True)
    next_of_kin_address = models.TextField(verbose_name="Address")
    next_of_kin_suburb = models.CharField(max_length=50, verbose_name="Suburb/Town")
    next_of_kin_state = models.ForeignKey(State, verbose_name="State/Province/Territory", related_name="next_of_kin_set")
    next_of_kin_postcode = models.IntegerField(verbose_name="Postcode")
    next_of_kin_home_phone = models.CharField(max_length=30, blank=True, null=True, verbose_name="home phone")
    next_of_kin_mobile_phone = models.CharField(max_length=30, blank=True, null=True, verbose_name="mobile phone")
    next_of_kin_work_phone = models.CharField(max_length=30, blank=True, null=True, verbose_name="work phone")
    next_of_kin_email = models.EmailField(blank=True, null=True, verbose_name="email")
    doctors = models.ManyToManyField(Doctor, through="PatientDoctor")
    active = models.BooleanField(default=True, help_text="Ticked if active in the registry, ie not a deleted record, or deceased patient.")

    class Meta:
        ordering = ["family_name", "given_names", "date_of_birth"]
        # 2010-07-26 added uniqueness of family_name, given_names in the same group
        unique_together = ("family_name", "given_names", "working_group")

    def __unicode__(self):
        if self.active:
            return "%s %s" % (self.family_name, self.given_names)
        else:
            return "%s %s (Archived)" % (self.family_name, self.given_names)

    def save(self, *args, **kwargs):
        # store the field in uppercase in the DB
        if hasattr(self, 'family_name'):
            self.family_name = stripspaces(self.family_name).upper()

        if hasattr(self, 'given_names'):
            self.given_names = stripspaces(self.given_names)

        if not self.pk:
            self.active = True
        super(Patient, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        """
        If a user deletes a patient it's active flag will be true, so we should set it to false.
        If a superuser deletes a patient it's active flag is false, so we should delete the object.
        """
        if self.active:
            logger.debug("Archiving patient record.")
            self.active = False
            self.save()
        else:
            logger.debug("Deleting patient record.")
            super(Patient, self).delete(*args, **kwargs)


class PatientDoctor(models.Model):
    patient = models.ForeignKey(Patient)
    doctor = models.ForeignKey(Doctor)
    relationship = models.CharField(max_length=50)

    class Meta:
        verbose_name = "medical professionals for patient"
        verbose_name_plural = "medical professionals for patient"
