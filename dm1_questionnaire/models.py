# -*- coding: utf-8 -*-
# vim: set fileencoding=UTF-8:
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from dm1 import base
from groups.models import WorkingGroup
from patients.models import Country, State

import dm1.models
import patients.models


class ApproveMixin(object):
    """
    A mixin that can be dropped in to add an approve() method to a Django model
    which will copy the instance to another model.
    """

    def approve(self, approve_class, commit=False, delete=False, keys=False, **kwargs):
        """
        Copies the fields on the model instance over to a new record on
        another, similarly defined model.

        Parameters:

        approve_class - The model to copy the data to.
        commit        - True to call save() on the new model instance.
        delete        - True to call self.delete() once the work is done. You
                        probably don't want to use this without also defining
                        commit.
        keys          - True to also copy keys over.
        **kwargs      - Any additional fields to be added can be specified via
                        extra keyword arguments in the form "field=value".
        """

        o = approve_class()

        for field in self._meta.fields:
            # Skip AutoFields and (optionally) keys.
            if not (field.auto_created or (field.rel and not keys)):
                setattr(o, field.name, getattr(self, field.name))

        for field, value in kwargs.iteritems():
            setattr(o, field, value)

        if commit:
            o.save()

        if delete:
            self.delete()

        return o


class Patient(ApproveMixin, models.Model):
    SEX_CHOICES = (
        ("M", "Male"),
        ("F", "Female"),
        #("X", "Other/Intersex"), # Trac 16 Item 9
    )

    working_group = models.ForeignKey(WorkingGroup, related_name="dm1_questionnaire_patient_set")
    family_name = models.CharField(max_length=100, db_index=True)
    given_names = models.CharField(max_length=100, db_index=True)
    date_of_birth = models.DateField()
    sex = models.CharField(max_length=1, choices=SEX_CHOICES)
    address = models.TextField()
    suburb = models.CharField(max_length=50, verbose_name="Suburb/Town")
    state = models.ForeignKey(State, verbose_name="State/Province/Territory", related_name="dm1_questionnaire_patient_set")
    country = models.ForeignKey(Country, related_name="dm1_questionnaire_patient_set")
    postcode = models.IntegerField()
    home_phone = models.CharField(max_length=30, blank=True, null=True)
    mobile_phone = models.CharField(max_length=30, blank=True, null=True)
    work_phone = models.CharField(max_length=30, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    
    class Meta:
        ordering = ["family_name", "given_names", "date_of_birth"]
        verbose_name = "Online Questionnaire"   # Appears in Admin UI: Site Administration

    def __unicode__(self):
        return "%s %s" % (self.family_name.upper(), self.given_names)

    def approve(self):
        o = super(Patient, self).approve(patients.models.Patient, keys=True)

        # Handle next of kin fields by copying the patient details for now.
        fields = (
            ("family_name", "next_of_kin_family_name"),
            ("given_names", "next_of_kin_given_names"),
            ("address", "next_of_kin_address"),
            ("suburb", "next_of_kin_suburb"),
            ("state", "next_of_kin_state"),
            ("postcode", "next_of_kin_postcode"),
            ("home_phone", "next_of_kin_home_phone"),
            ("mobile_phone", "next_of_kin_mobile_phone"),
            ("work_phone", "next_of_kin_work_phone"),
            ("email", "next_of_kin_email"),
        )
        for old, new in fields:
            setattr(o, new, getattr(self, old))
        
        o.save(force_insert=True)

        # Approve the diagnosis as well.
        try:
            self.diagnosis.approve(o)
        except Diagnosis.DoesNotExist:
            pass

        self.delete()

        return o


class Diagnosis(ApproveMixin, base.Diagnosis):
    patient = models.OneToOneField(Patient, primary_key=True)

    class Meta:
        #verbose_name_plural = "diagnoses"
        verbose_name = "patient completed questionnaire"

    def __unicode__(self):
        return unicode(self.patient)

    def approve(self, patient):
        diagnosis = super(Diagnosis, self).approve(dm1.models.Diagnosis, patient=patient, commit=True)

        # Loop through the models that have a one-to-one relationship with
        # this one and approve them. This is ugly, but effective.
        models = (
            MotorFunction,
            Surgery,
            Heart,
            HeartMedication,
            Respiratory,
            Muscle,
            MuscleMedication,
            FeedingFunction,
            Fatigue,
            FatigueMedication,
            SocioeconomicFactors,
            GeneralMedicalFactors,
            GeneticTestDetails,
            EthnicOrigin,
            ClinicalTrials,
        )
        for model in models:
            objects = model.objects.filter(diagnosis=self)
            for o in objects:
                o.approve(diagnosis)

        self.delete()

        return diagnosis


class MotorFunction(ApproveMixin, base.MotorFunction):
    diagnosis = models.OneToOneField(Diagnosis, primary_key=True)

    def __unicode__(self):
        return unicode(self.diagnosis)

    def approve(self, diagnosis):
        return super(MotorFunction, self).approve(dm1.models.MotorFunction, diagnosis=diagnosis, commit=True, delete=True)


class Surgery(ApproveMixin, base.Surgery):
    diagnosis = models.OneToOneField(Diagnosis, primary_key=True)

    def __unicode__(self):
        return unicode(self.diagnosis)

    def approve(self, diagnosis):
        return super(Surgery, self).approve(dm1.models.Surgery, diagnosis=diagnosis, commit=True, delete=True)


class Heart(ApproveMixin, base.Heart):
    diagnosis = models.OneToOneField(Diagnosis, primary_key=True)

    def __unicode__(self):
        return unicode(self.diagnosis)

    def approve(self, diagnosis):
        return super(Heart, self).approve(dm1.models.Heart, diagnosis=diagnosis, commit=True, delete=True)


class HeartMedication(ApproveMixin, base.HeartMedication):
    diagnosis = models.ForeignKey(Diagnosis, primary_key=True)

    def __unicode__(self):
        return unicode(self.diagnosis)

    def approve(self, diagnosis):
        return super(HeartMedication, self).approve(dm1.models.HeartMedication, diagnosis=diagnosis, commit=True, delete=True)


class Respiratory(ApproveMixin, base.Respiratory):
    diagnosis = models.OneToOneField(Diagnosis, primary_key=True)

    def __unicode__(self):
        return unicode(self.diagnosis)

    def approve(self, diagnosis):
        return super(Respiratory, self).approve(dm1.models.Respiratory, diagnosis=diagnosis, commit=True, delete=True)


class Muscle(ApproveMixin, base.Muscle):
    diagnosis = models.OneToOneField(Diagnosis, primary_key=True)

    def __unicode__(self):
        return unicode(self.diagnosis)

    def approve(self, diagnosis):
        return super(Muscle, self).approve(dm1.models.Muscle, diagnosis=diagnosis, commit=True, delete=True)


class MuscleMedication(ApproveMixin, base.MuscleMedication):
    diagnosis = models.ForeignKey(Diagnosis, primary_key=True)

    def __unicode__(self):
        return unicode(self.diagnosis)

    def approve(self, diagnosis):
        return super(MuscleMedication, self).approve(dm1.models.MuscleMedication, diagnosis=diagnosis, commit=True, delete=True)


class FeedingFunction(ApproveMixin, base.FeedingFunction):
    diagnosis = models.OneToOneField(Diagnosis, primary_key=True)

    def __unicode__(self):
        return unicode(self.diagnosis)

    def approve(self, diagnosis):
        return super(FeedingFunction, self).approve(dm1.models.FeedingFunction, diagnosis=diagnosis, commit=True, delete=True)


class Fatigue(ApproveMixin, base.Fatigue):
    diagnosis = models.OneToOneField(Diagnosis, primary_key=True)

    def __unicode__(self):
        return unicode(self.diagnosis)

    def approve(self, diagnosis):
        return super(Fatigue, self).approve(dm1.models.Fatigue, diagnosis=diagnosis, commit=True, delete=True)


class FatigueMedication(ApproveMixin, base.FatigueMedication):
    diagnosis = models.ForeignKey(Diagnosis, primary_key=True)

    def __unicode__(self):
        return unicode(self.diagnosis)

    def approve(self, diagnosis):
        return super(FatigueMedication, self).approve(dm1.models.FatigueMedication, diagnosis=diagnosis, commit=True, delete=True)


class SocioeconomicFactors(ApproveMixin, base.SocioeconomicFactors):
    diagnosis = models.OneToOneField(Diagnosis, primary_key=True)

    def __unicode__(self):
        return unicode(self.diagnosis)

    def approve(self, diagnosis):
        return super(SocioeconomicFactors, self).approve(dm1.models.SocioeconomicFactors, diagnosis=diagnosis, commit=True, delete=True)


class GeneralMedicalFactors(ApproveMixin, base.GeneralMedicalFactors):
    diagnosis = models.OneToOneField(Diagnosis, primary_key=True)

    def __unicode__(self):
        return unicode(self.diagnosis)

    def approve(self, diagnosis):
        return super(GeneralMedicalFactors, self).approve(dm1.models.GeneralMedicalFactors, diagnosis=diagnosis, commit=True, delete=True)


class GeneticTestDetails(ApproveMixin, base.GeneticTestDetails):
    diagnosis = models.OneToOneField(Diagnosis, primary_key=True)

    def __unicode__(self):
        return unicode(self.diagnosis)

    def approve(self, diagnosis):
        return super(GeneticTestDetails, self).approve(dm1.models.GeneticTestDetails, diagnosis=diagnosis, commit=True, delete=True)


class EthnicOrigin(ApproveMixin, base.EthnicOrigin):
    diagnosis = models.OneToOneField(Diagnosis, primary_key=True)

    def __unicode__(self):
        return unicode(self.diagnosis)

    def approve(self, diagnosis):
        return super(EthnicOrigin, self).approve(dm1.models.EthnicOrigin, diagnosis=diagnosis, commit=True, delete=True)


class ClinicalTrials(ApproveMixin, base.ClinicalTrials):
    diagnosis = models.ForeignKey(Diagnosis, primary_key=True)

    def __unicode__(self):
        return unicode(self.diagnosis)

    def approve(self, diagnosis):
        return super(ClinicalTrials, self).approve(dm1.models.ClinicalTrials, diagnosis=diagnosis, commit=True, delete=True)
